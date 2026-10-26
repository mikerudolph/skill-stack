#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.metadata
import os
import subprocess
import sys
import tempfile
import venv
import xml.etree.ElementTree as ET
from pathlib import Path


PAGE_WIDTH = "420mm"
PAGE_HEIGHT = "210mm"
PAGE_VIEWBOX = "0 0 420 210"
REQUIRED_IDS = {
    "page",
    "design-tokens",
    "design-style",
    "sheet-frame",
    "zone-grid",
    "title-block",
    "diagram-title",
    "diagram-subject",
    "diagram-revision",
    "diagram-date",
    "diagram-sheet",
}
REQUIRED_TOKENS = {
    "#263445",
    "#286DA8",
    "#617184",
    "#F3F5F7",
    "#2F7D5B",
    "#C74634",
    "#A96500",
    "#FFFFFF",
    "Helvetica",
    "Courier",
}
RENDERER_VERSION = "2.3.2"
REPORTLAB_VERSION = "5.1.0"
TEMPLATE_CLASSES = {
    "frame",
    "panel",
    "panel-head",
    "ink",
    "blue",
    "muted",
    "added",
    "removed",
    "attention",
    "paper",
    "soft",
    "line",
    "link",
    "optional",
    "arrowhead",
    "arrowhead-muted",
    "label",
    "small",
    "body",
    "heading",
    "mono",
    "zone",
    "box",
    "note",
    "tab",
    "tab-letter",
    "subheading",
    "annotation",
    "rule",
    "guide",
}


def renderer_python(cache_dir: Path | None) -> Path:
    python_path = "Scripts/python.exe" if os.name == "nt" else "bin/python"
    if cache_dir is not None:
        return cache_dir / python_path
    cache_root = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache"))
    return cache_root / "skill-stack" / "create-diagram" / python_path


def renderer_ready(python_path: Path) -> bool:
    probe = (
        "import importlib.metadata, sys; "
        f"sys.exit(0 if importlib.metadata.version('svglib') == '{RENDERER_VERSION}' "
        f"and importlib.metadata.version('reportlab') == '{REPORTLAB_VERSION}' else 1)"
    )
    result = subprocess.run(
        [str(python_path), "-c", probe],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def element_signature(element: ET.Element, dynamic_text_ids: set[str]) -> tuple:
    element_id = element.attrib.get("id")
    attributes = tuple(
        sorted(
            (name, value)
            for name, value in element.attrib.items()
            if name != "data-placeholder"
        )
    )
    if element_id in dynamic_text_ids:
        text = ""
    elif element_id == "design-style":
        text = " ".join((element.text or "").split())
    else:
        text = (element.text or "").strip()
    children = (
        ()
        if element_id in dynamic_text_ids
        else tuple(element_signature(child, dynamic_text_ids) for child in element)
    )
    return element.tag, attributes, text, children


def use_renderer(args: list[str], cache_dir: Path | None) -> int | None:
    target_python = renderer_python(cache_dir)
    target_environment = target_python.parent.parent
    current_environment = Path(sys.prefix)
    if (
        current_environment.resolve() == target_environment.resolve()
        and renderer_ready(target_python)
    ):
        return None

    try:
        if not target_python.is_file():
            venv.create(target_environment, with_pip=True)
        if not target_python.is_file():
            raise OSError("Python did not create the renderer environment.")
        if not renderer_ready(target_python):
            requirements = Path(__file__).resolve().parents[1] / "requirements.txt"
            print("Install the pinned SVG-to-PDF renderer in the user cache.")
            subprocess.run(
                [
                    str(target_python),
                    "-m",
                    "pip",
                    "install",
                    "--disable-pip-version-check",
                    "--no-input",
                    "--only-binary=:all:",
                    "--timeout",
                    "15",
                    "--retries",
                    "2",
                    "-r",
                    str(requirements),
                ],
                check=True,
            )
        if not renderer_ready(target_python):
            raise OSError(f"svglib {RENDERER_VERSION} is not ready.")
    except (OSError, subprocess.CalledProcessError) as error:
        print(f"PDF renderer setup failed: {error}", file=sys.stderr)
        return 1

    return subprocess.run(
        [str(target_python), str(Path(__file__).resolve()), *args],
        check=False,
    ).returncode


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert the standard diagram SVG sheet to a PDF."
    )
    parser.add_argument("source", type=Path, help="Path to the completed SVG sheet.")
    parser.add_argument("output", type=Path, help="Path for the PDF file.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace the output file when it exists.",
    )
    parser.add_argument(
        "--custom-design",
        action="store_true",
        help="Allow a design that differs from the standard sheet.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        help="Store the renderer environment in this folder.",
    )
    return parser.parse_args()


def validate_svg(source: Path, custom_design: bool) -> bytes:
    try:
        data = source.read_bytes()
        root = ET.fromstring(data)
    except OSError as error:
        raise ValueError(f"Cannot read the SVG file: {error}") from error
    except ET.ParseError as error:
        raise ValueError(f"The SVG file has invalid XML: {error}") from error

    if not root.tag.endswith("svg"):
        raise ValueError("The source file must have an SVG root element.")

    if not custom_design:
        if root.attrib.get("width") != PAGE_WIDTH:
            raise ValueError(f"Set the SVG width to {PAGE_WIDTH}.")
        if root.attrib.get("height") != PAGE_HEIGHT:
            raise ValueError(f"Set the SVG height to {PAGE_HEIGHT}.")
        if " ".join(root.attrib.get("viewBox", "").split()) != PAGE_VIEWBOX:
            raise ValueError(f"Set the SVG viewBox to {PAGE_VIEWBOX}.")

    elements = list(root.iter())
    if not custom_design:
        template_path = Path(__file__).resolve().parents[1] / "assets" / "diagram-template.svg"
        template_root = ET.parse(template_path).getroot()
        ids = {element.attrib["id"] for element in elements if "id" in element.attrib}
        missing_ids = sorted(REQUIRED_IDS - ids)
        if missing_ids:
            raise ValueError("The SVG is missing required template elements: " + ", ".join(missing_ids))

        token_element = next(
            element for element in elements if element.attrib.get("id") == "design-tokens"
        )
        style_element = next(
            element for element in elements if element.attrib.get("id") == "design-style"
        )
        token_text = " ".join(token_element.itertext())
        style_text = " ".join(style_element.itertext())
        missing_tokens = sorted(token for token in REQUIRED_TOKENS if token not in token_text)
        if missing_tokens:
            raise ValueError("The SVG is missing standard design tokens: " + ", ".join(missing_tokens))
        missing_styles = sorted(token for token in REQUIRED_TOKENS if token not in style_text)
        if missing_styles:
            raise ValueError("The SVG style is missing standard values: " + ", ".join(missing_styles))

        standard_ids = {
            "design-tokens",
            "design-style",
            "sheet-frame",
            "zone-grid",
            "title-block",
        }
        standard_elements = {
            element.attrib["id"]: element
            for element in template_root.iter()
            if element.attrib.get("id") in standard_ids
        }
        diagram_elements = {
            element.attrib["id"]: element
            for element in elements
            if element.attrib.get("id") in standard_elements
        }
        dynamic_ids = {
            "diagram-title",
            "diagram-subject",
            "diagram-revision",
            "diagram-date",
            "diagram-sheet",
        }
        changed_elements = [
            element_id
            for element_id, standard_element in standard_elements.items()
            if element_signature(standard_element, dynamic_ids)
            != element_signature(diagram_elements[element_id], dynamic_ids)
        ]
        if changed_elements:
            raise ValueError("Restore the standard sheet elements: " + ", ".join(changed_elements))

        style_count = sum(element.tag.endswith("style") for element in elements)
        if style_count != 1:
            raise ValueError("Keep one standard style element in the SVG.")

        palette = {token for token in REQUIRED_TOKENS if token.startswith("#")}
        for element in elements:
            if {"style", "font-family", "font-size", "font-weight"} & element.attrib.keys():
                raise ValueError("Use a standard template class for each text and shape style.")
            classes = set(element.attrib.get("class", "").split())
            if classes - TEMPLATE_CLASSES:
                invalid_classes = ", ".join(sorted(classes - TEMPLATE_CLASSES))
                raise ValueError("Use only standard template classes: " + invalid_classes)
            for name in ("fill", "stroke"):
                value = element.attrib.get(name)
                if value is not None and value not in palette | {"none"}:
                    raise ValueError(f"Use a standard color for {name}: {value}")

    placeholders = [
        element.attrib.get("id", element.tag)
        for element in elements
        if element.attrib.get("data-placeholder") == "true"
    ]
    if placeholders:
        raise ValueError("Replace or remove the template prompts: " + ", ".join(placeholders))

    return data


def render(source: Path, output: Path, force: bool, custom_design: bool) -> None:
    source_path = source.resolve()
    output_path = output.resolve()
    if source_path == output_path:
        raise ValueError("Use a different path for the SVG and PDF files.")
    if not source_path.is_file():
        raise ValueError(f"The SVG file does not exist: {source_path}")
    if output_path.exists() and not force:
        raise ValueError(f"The PDF file exists. Use --force to replace it: {output_path}")
    if output_path.suffix.lower() != ".pdf":
        raise ValueError("The output file name must end with .pdf.")
    if source_path.suffix.lower() != ".svg":
        raise ValueError("The source file name must end with .svg.")

    validate_svg(source_path, custom_design)
    try:
        from reportlab.graphics import renderPDF
        from svglib.svglib import svg2rlg
    except ImportError as error:
        raise ValueError("The SVG-to-PDF renderer is not available.") from error

    if importlib.metadata.version("svglib") != RENDERER_VERSION:
        raise ValueError(f"svglib {RENDERER_VERSION} is required.")
    if importlib.metadata.version("reportlab") != REPORTLAB_VERSION:
        raise ValueError(f"ReportLab {REPORTLAB_VERSION} is required.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix="diagram-", suffix=".pdf", dir=output_path.parent, delete=False
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)
        try:
            drawing = svg2rlg(str(source_path))
            if drawing is None:
                raise ValueError("The renderer could not read the SVG drawing.")
            if not custom_design:
                page_width = 420 * 72 / 25.4
                page_height = 210 * 72 / 25.4
                if abs(drawing.width - page_width) > 0.1 or abs(drawing.height - page_height) > 0.1:
                    raise ValueError("The renderer found an unexpected SVG page size.")
            renderPDF.drawToFile(drawing, str(temporary_path), title=source_path.stem)
        except Exception as error:
            raise ValueError(f"The SVG-to-PDF renderer failed: {error}") from error
        if not temporary_path.read_bytes().startswith(b"%PDF-"):
            raise ValueError("The renderer did not create a valid PDF file.")
        temporary_path.replace(output_path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


def preflight(args: argparse.Namespace) -> None:
    source_path = args.source.resolve()
    output_path = args.output.resolve()
    if source_path == output_path:
        raise ValueError("Use a different path for the SVG and PDF files.")
    if not source_path.is_file():
        raise ValueError(f"The SVG file does not exist: {source_path}")
    if output_path.exists() and not args.force:
        raise ValueError(f"The PDF file exists. Use --force to replace it: {output_path}")
    if output_path.suffix.lower() != ".pdf":
        raise ValueError("The output file name must end with .pdf.")
    if source_path.suffix.lower() != ".svg":
        raise ValueError("The source file name must end with .svg.")
    validate_svg(source_path, args.custom_design)


def main() -> int:
    args = parse_args()
    try:
        preflight(args)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    renderer_status = use_renderer(sys.argv[1:], args.cache_dir)
    if renderer_status is not None:
        return renderer_status
    try:
        render(args.source, args.output, args.force, args.custom_design)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    print(f"Created PDF: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
