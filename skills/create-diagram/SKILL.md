---
name: create-diagram
description: Create detailed technical explanation sheets as PDFs. Use source code to explain architecture, data flow, state changes, failures, and design constraints with diagrams, tables, and annotations.
---

# Create a diagram

Create a diagram that explains the requested system, behavior, or change.
The result must help a technical reader understand the mechanism without a separate explanation.
Use diagrams, annotated examples, comparison tables, and technical details that support the main subject.
Use this skill for codebase components, architecture, data flow, workflows, and pull request changes.
Use ASD-STE100 Issue 9 for all text in the diagram and its title block.

## Required output

Deliver the final diagram as a PDF.
Do not deliver an image or source file in place of the PDF.
Save the PDF in a scratchpad inside the active working repository.
Use `<repo>/.scratchpad/diagrams/` when the task runs inside a Git repository.
Otherwise, use `./.scratchpad/diagrams/` in the working directory.
Do not save the final PDF in `/private/`, `/tmp/`, or another system temporary directory.
Use the standard design in this skill unless the user asks for a different design.
Do not use the repository's colors, fonts, or diagram theme unless the user asks for them.
Keep an editable source file with the PDF only when the user asks for it or when it helps future edits.
Use `--custom-design` only when the user asks for a different design.

## Read the subject

For a codebase diagram, inspect the files that define the subject and its direct connections.
For a pull request diagram, inspect the full diff and the related code.
Show the source revision or pull request identifier when the user provides it.
Distinguish current behavior from proposed behavior.
Mark changed, added, and removed parts with both a label or shape and a color.
Do not infer behavior that the code or user does not support.

## Develop the technical explanation

Select the reader question before you select panel titles.
For example: "When does a write become visible, and what happens if two writers use the same version?"
Trace one concrete operation from its input to its visible result.
Read the implementation at each important boundary, including storage operations and error handling.
Use documentation for context, then check its claims against the implementation.

Prepare the content before you draw the sheet:

- Identify the input, output, responsible component, and state change at each step.
- Record important data fields, interfaces, conditions, and transaction boundaries.
- Explain the mechanism that preserves each important constraint.
- Show applicable failure conditions, partial effects, retry behavior, and recovery steps.
- Give a concrete example with values that shows the mechanism.
- Record a source file and symbol for each technical claim.
- Identify evidence limits, including tests that you inspected but did not run.

Keep this content with the working files until the review is complete.
Do not use broad statements such as "Store data safely" without the checks and ordering that make the statement useful.
For a transaction, show its checks, writes, commit boundary, and rollback effects.
For a cache, show its validity check, rebuild inputs, and relation to durable state.
For concurrency, show which condition rejects an operation and what the caller must do next.
Apply these examples only when they fit the subject.
Do not invent details to fill the sheet.

Give each panel a different explanatory function.
Use a structure diagram for responsibilities, a sequence for ordering, and a table for conditions and results.
Use annotations to explain why a step or boundary matters.
Use short source identifiers on the sheet and connect them to file paths and symbols in a source area.
Label hypothetical values as an example.
State a design consequence as an inference when the source does not state it directly.
Use one level of detail within each panel.
Connect an overview to implementation details with matching step numbers, component names, or source identifiers.
Select the diagram type that best explains these relationships.
Use a component or context diagram for structure.
Use a sequence or flow diagram for behavior over time.
Use a data flow diagram for data movement.
Use a state diagram for state changes.
Use a dependency diagram for build or package relationships.
Combine types only when one type cannot explain the subject clearly.

## Standard design

Use the custom 2:1 landscape sheet in [assets/diagram-template.svg](assets/diagram-template.svg).
The sheet is 420 mm by 210 mm and has one page.
Use its frame, coordinate labels, panel shapes, title block, fonts, and colors.
Do not change its design tokens or page dimensions.
Do not claim that the custom sheet complies with ISO 5457.

Use ISO 5457 as guidance for the sheet frame and zones.
Use ISO 128-2 as guidance for line types and connectors.
Use ISO 7200 as guidance for title block fields.
Use the C4 model levels for software architecture when they fit the subject.
Treat these standards and models as design guides.

Use six panels when the subject benefits from an overview with separate topics.
Place panels A, B, and C in the top row.
Place panels D, E, and F in the bottom row.
Use panel B for the main mechanism when the layout supports that choice.
For example, use A for structure, B for the mechanism, C for conditions, D for failures, E for recovery, and F for sources.
These are explanatory functions, not required panel titles.
Do not allocate a large panel to a legend or a few general statements.
Give each panel a letter and a short title.
Delete or merge panels that add no value.
Do not add empty panels to reach six.
Keep the title block at the lower right of the sheet.
Include the diagram title, subject, date, and sheet number.
Include the source revision or pull request identifier when it applies.
Use a clear value such as `Not supplied` for missing title block data.

The template has fixed colors and fonts.
Use Helvetica for labels and body text.
Use bold Helvetica for panel titles and section labels.
Use Courier for paths, identifiers, and revision values.
Use dark text on light fills.
Do not use color as the only signal.
Pair each status color with a word, symbol, line type, or shape.
Keep borders and connector lines thin.
Use solid lines for direct relationships.
Use dashed lines for optional or proposed relationships.
Add arrowheads to show direction.
Draw each arrowhead as a filled triangle from the `arrowhead` or `arrowhead-muted` class.
Label each relationship with a short verb phrase.
Explain unfamiliar symbols, line types, and status marks in a compact legend when necessary.
Use white panel headers with dark letter tabs.
Use thin rules, alternate table row fills, and blue annotations for technical emphasis.
Keep body lines approximately 4 mm apart and table rows approximately 6 to 9 mm high.
Increase row height when a cell needs multiple lines.
Use the `subheading`, `annotation`, `rule`, and `guide` classes for sections and callouts.
Do not stretch a short list across a large panel.
If a panel has little content, reduce its area or use that area for a necessary detail.
Do not add repeated text or decoration to increase density.

## Build the PDF

Use the same SVG-to-PDF path for every diagram.
Do not select a different diagram tool or export method for each task.
Set `skill_dir` to the absolute path of the folder that contains this `SKILL.md`.
Follow the active repository's output rules.
Set `diagram_pdf` to `<repo>/.scratchpad/diagrams/<short-title>.pdf`.
Use `./.scratchpad/diagrams/<short-title>.pdf` when the task is not inside a Git repository.
Use a different path only when the user gives one or repository rules require it.
Use a lower-case `.pdf` suffix.
Add it when the user path has no suffix.
Replace a different suffix with `.pdf`.
Set `diagram_svg` to the same path with the `.svg` extension.
Do not overwrite an existing PDF.
Add `-2`, `-3`, or the next number to the short title if the PDF path exists.
If the PDF exists from this task, use `--force` to replace it after an edit.

1. Create the output directory and copy the template to the working SVG path:

   ```sh
   diagram_pdf=".scratchpad/diagrams/<short-title>.pdf"
   diagram_svg="${diagram_pdf%.pdf}.svg"
   mkdir -p "$(dirname "$diagram_pdf")"
   cp "$skill_dir/assets/diagram-template.svg" "$diagram_svg"
   ```

2. Edit the copy to add the diagram and its text.
3. Add diagram elements inside the selected panel groups.
4. Treat one viewBox unit as one millimeter.
5. Use the SVG classes in the template.
   Do not add style rules, inline styles, or new classes.
   Draw arrowheads as polygons with the `arrowhead` or `arrowhead-muted` class.
6. Keep the page size, frame, coordinate labels, title block, fonts, and colors from the template.
7. Run the renderer:

   ```sh
   python3 "$skill_dir/scripts/render_pdf.py" "$diagram_svg" "$diagram_pdf"
   ```

   For a user-requested design, append `--custom-design` to this command.

8. Render the PDF to a PNG with Poppler or an available PDF renderer.
   Inspect the PNG at full-sheet size and at a readable detail scale.
9. Complete the content and visual reviews below.
   Correct content failures and clipped, overlapping, or unreadable content in the SVG.
10. Run the same renderer with `--force` after each change.
11. Keep the working SVG until the review is complete.
    Remove it unless the user asks for an editable source file or further edits are expected.

The renderer checks the SVG page size, design values, and required template elements.
It rejects template prompts that remain in the SVG.
It creates a vector PDF with the fixed page size.
On first use, the renderer installs svglib 2.3.2 and ReportLab 5.1.0 in a separate user cache.
Later runs use that cached version.
The first use needs internet access to get the pinned package.
The renderer does not add its environment to the active repository.
Use `--cache-dir PATH` only when the environment needs a specific writable cache folder.
If the renderer cannot run, report the missing dependency or conversion error.
Do not substitute a different export method.

## Diagram content

Give the diagram a title that states its type and scope.
Show only the elements needed to explain the subject.
Group elements by system, layer, owner, or process when this helps the reader.
Name each element and give it a short role or state.
Use one direction for each connector.
Show external systems and boundaries when they affect the subject.
Show protocols, formats, or interfaces when they affect a relationship.
Explain abbreviations in the diagram or its legend.
Use labels that readers can understand without a spoken explanation.

For a pull request diagram, show the behavior before and after the change when both states matter.
Connect changed files to affected components when the diff supports that link.
Show tests or verification paths only when the diff or repository confirms them.
Do not imply that a change is tested or complete without evidence.

Keep a clear reading order from left to right, then from top to bottom.
Use alignment and spacing to show groups.
Keep connectors outside labels and avoid crossings when possible.
Use a connector bridge or a clear crossing mark when lines must cross.
Keep text large enough to read at normal page size.
Use `label` for body text and `body` for compact table cells and detailed explanations.
Use the `small` text class for metadata and notes only.
Use a separate PDF for a different diagram view.

## Review the result

Review the technical content separately from the visual design.
A successful PDF export does not prove that the explanation is useful.

The content review must answer these questions from the sheet alone:

- What operation or decision does the sheet explain?
- What data moves, and which state changes?
- Which checks, ordering rules, or boundaries control the result?
- Why does the mechanism have those rules?
- What happens in the important failure or competing-operation case?
- Which concrete example demonstrates the result?
- Where can the reader verify the claims?

If a question does not apply, use a subject-specific question with comparable technical depth.
Reject a sheet that contains only component names, general benefits, or repeated summaries.
Do not remove important details only to keep the first layout.
Change the panel allocation or create a separate detail sheet when necessary.

Compare the rendered sheet with the user's visual reference when one is available.
Check panel proportions, typography, table density, annotations, and use of space.
Check that each arrow identifies an operation, data transfer, or state transition.
Check that the source area and title block remain readable.
Check that no text crosses a panel, cell, connector, or page boundary.
Do not deliver the PDF until both reviews pass.
Report source inspection and executed tests separately.

## Language

Use ASD-STE100 Issue 9 for titles, labels, notes, legend text, and title block text.
Use one term for each concept.
Use the same label for the same component in all panels.
Use short command forms for instructions.
Use direct, active sentences.
Keep each sentence within the applicable STE word limit.
Keep technical names, code paths, and identifiers unchanged when they must match the source.
Explain unfamiliar technical terms in the legend or a panel.

## Technical terms for this skill

These terms apply to this skill.
Use category 19 of rule 1.5 for software nouns and category 15 for document nouns.

| Term | Part of speech | Meaning and category |
| --- | --- | --- |
| diagram | Noun | A visual model of elements and their relationships. Category 15. |
| PDF | Noun | Portable Document Format, the required output file. Category 15. |
| SVG | Noun | Scalable Vector Graphics, the editable diagram format. Category 15. |
| viewBox | Noun | The SVG area that defines drawing coordinates. Category 15. |
| design token | Noun | A fixed value for a color, font, or line style. Category 19. |
| panel | Noun | A framed area that has one topic. Category 15. |
| title block | Noun | A group of document fields that identify a drawing. Category 15. |
| connector | Noun | A line that shows a relationship or direction. Category 19. |
| legend | Noun | A key that explains symbols, lines, and colors. Category 15. |
| revision | Noun | An identified state of a file or project. Category 19. |
| pull request | Noun | A proposal to add repository changes. Category 19. |
| source revision | Noun | The commit or version used as evidence for a diagram. Category 19. |
| user cache | Noun | A local folder for files that software uses again. Category 19. |
| svglib | Noun | The pinned software that converts the SVG sheet to PDF. Category 19. |
| ReportLab | Noun | The software that creates the PDF from the SVG drawing. Category 19. |
| export | Noun, verb | As a noun, a generated file. As a verb, create a file in a target format. Categories 15 and 2. |
