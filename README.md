# skill-stack

Personal skills for Claude Code and Codex.
Use Git to keep one source on each machine.

## Skills

- [new-repo](skills/new-repo/SKILL.md): prepare repositories with product goals, agent instructions, permanent decision records, verification, and ASD-STE100 language rules.

## File structure

```text
skills/
  new-repo/
    SKILL.md
    assets/
```

Put `name` and `description` in the YAML frontmatter of `SKILL.md`.
Write the skill instructions after the frontmatter.
Use the same name for the skill and its directory.
Keep output templates in `assets/`.
Do not add a reference directory or reference files.

Use the [Codex skill instructions](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill instructions](https://code.claude.com/docs/en/skills).

## Install on each machine

Clone this repository into a directory that you will keep.
Use a symlink for each skill in these personal directories:

| Agent | Personal skill directory | Project skill directory |
| --- | --- | --- |
| Codex | `~/.agents/skills/<skill-name>/` | `.agents/skills/<skill-name>/` |
| Claude Code | `~/.claude/skills/<skill-name>/` | `.claude/skills/<skill-name>/` |

The two agents can read skill directories through symlinks.
Refer to [Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) and [Claude Code skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load).

Use these commands from the repository root:

```sh
skill="new-repo"
source_dir="$(pwd -P)/skills/$skill"

if [ ! -f "$source_dir/SKILL.md" ]; then
  printf 'Missing skill: %s\n' "$source_dir/SKILL.md" >&2
else
  for skills_dir in "$HOME/.agents/skills" "$HOME/.claude/skills"; do
    destination="$skills_dir/$skill"
    if [ -e "$destination" ] || [ -L "$destination" ]; then
      printf 'Kept entry: %s\n' "$destination"
    else
      mkdir -p "$skills_dir" && ln -s "$source_dir" "$destination"
    fi
  done
fi
```

These commands keep entries that are in the destination, with broken symlinks.
Use the procedure for each skill on each machine.
Keep the source directory in place.

On each machine, use `git pull` to update the skill files.
Add symlinks for new skills separately.
If an agent cannot find a change, start a new agent session.

## Language and work rules

Use [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) for all new or changed human-readable text.
This includes skill instructions, templates, decisions, permitted comments, commit messages, pull requests, and agent responses.
The [repository instructions](AGENTS.md) give the language review requirements.

Use paths that are correct on all machines.
Give prerequisites and configuration requirements for each skill.
Do not add credentials, private data, or generated output to this repository.
Make helper scripts safe to use again.
