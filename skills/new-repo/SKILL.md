---
name: new-repo
description: Prepare a new repository with product goals, agent instructions, decision history, and ASD-STE100 language rules. Also use when the user wants these rules in a repository.
---

# New repo

Use the repository rules from Artifacts to prepare a new repository.
Keep the decision history in `AGENTS.md`.
Add a new decision to change a previous decision.
Do not change a recorded decision record.

## Use ASD-STE100

Use [ASD-STE100 Issue 9, dated 2025-01-15](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) for all new or changed human-readable text.
This rule includes this skill, its metadata, and its templates.
Apply the rule to these items:

- Repository documents, goals, decisions, and task instructions.
- Permitted comments, documentation strings, test descriptions, and example text.
- User interface text, help text, and error messages.
- Commit messages, issue text, pull requests, and review comments.
- Plans, progress messages, and completion responses about repository work.
- Text from scripts, tools, and document generators that the project controls.

Before you write, read the applicable rules and dictionary entries in that issue.
Use a local copy from ASD or get the PDF from ASD.
Do not add the standard or a dictionary copy to the repository.
If you cannot get the standard, record `STE review: not completed`.
Give the cause.

Continue other work.
Do not record STE compliance without the review.

Apply these language controls:

- Select dictionary words with the correct meanings, parts of speech, and permitted forms.
- Use applicable technical nouns and technical verbs that obey rules 1.5 and 1.12.
- Record project-specific technical terms, meanings, parts of speech, and rule categories in `AGENTS.md`.
- Keep one term for each concept. Do not use the term table for general words that STE rejects.
- Limit instruction sentences to 20 words. Limit description sentences to 25 words.
- Use command forms for instructions. Put a necessary condition before its command.
- Give one action per sentence, except for actions that must occur together.
- Use active constructions and permitted verb tenses. Prevent unclear pronouns, contractions, and phrasal verbs.
- Use American English spelling.
- Keep multi-word nouns within three words. For longer technical nouns, obey rule 2.2.
- Keep paragraphs to one topic and six sentences. Use STE word-count rules and punctuation rules.

Use the full standard for the review. These controls are not a replacement for it.
A sentence-length check is not a full STE review.

Keep necessary identifiers, commands, paths, protocol values, and quotations without changes.
Use STE for their explanations.
Use approved terms for new identifiers when their syntax and interfaces let you select the words.
Do not change a necessary literal value only to use dictionary words.
Do not change legal text or third-party quotations that must keep their initial form.

Do not change previous decision records or their evidence.
For a repository with files, add a new decision that adds the language rule.
Apply STE to that decision and subsequent text.
Do not change decision history for language corrections.

Complete the STE review before you give the result to the user.
Record the standard issue, review method, result, and remaining terms or rule questions.
If the repository has an STE checker, include it in the repository checks.
Also do an STE review of meaning and technical terms.
Record `STE review: not completed` if you cannot complete the review.
Do not record full STE compliance from a checker result only.

## Find the task scope

Read the destination files, applicable instructions, Git status, and user requirements first.
Use the available context to identify the product purpose and tool requirements.
Get missing choices from the user only when they change the work.
Do not change other user work.
Make a remote repository, push, or deployment only when the user instructions include that action.
Apply the same rule to product implementation.

Use tools for the selected software stack.
Select architecture, dependencies, limits, and deployment methods for the new product.
Do not copy the Artifacts architecture into a different project.

## Prepare the repository documents

Read [assets/AGENTS.md](assets/AGENTS.md) and [assets/GOALS.md](assets/GOALS.md) before you prepare the destination documents.
Adapt the templates to the project.
Replace each `{{...}}` field with project text in STE.
Remove sections that do not apply.
Connect document links only to files in the repository.

Identify open choices.
Do not give a product commitment without user approval.

Use these document functions:

- `GOALS.md` gives the purpose, users, priorities, scope limits, and acceptance criteria.
- `AGENTS.md` gives context links, the decision register, work rules, language rules, technical terms, and verification commands.
- `README.md` gives the project description, prerequisites, setup, and commands to operate the project and do checks.

Keep one copy of each explanation in its applicable document.
Connect other documents to that explanation with links.

For Claude Code, put `@AGENTS.md` in a root `CLAUDE.md`.
Add the import to a file in the destination without removal of other instructions.
Keep one decision register in `AGENTS.md`.
The import uses [Claude Code's shared-file method](https://code.claude.com/docs/en/memory#share-one-file-with-other-coding-tools).

Adapt [assets/pull_request_template.md](assets/pull_request_template.md) for the selected repository host.
For GitHub, put the result in `.github/pull_request_template.md`.
Include the change, verification results, and STE review result.
Do not add host-specific files when the host choice is open.

Add tickets, review directories, service resources, or project skills only when the task makes them necessary.

## Prepare the decision register

For a new repository, start at D1.
The template gives the initial decisions for work rules and language rules.
Adapt these draft decisions before their first use as repository records.

Add product or architecture decisions only after the choice occurs.
Use the date when you record the decision.
Do not give a date for a previous choice without evidence.
Do not put proposals or open questions in the decision register.

For a repository with files, read all decisions and their supporting files first.
Do not change those entries or files.
Continue after the highest recorded ID.
Add an amendment when a new work rule changes an recorded rule.
Make the work instructions agree with the resulting rule.

Apply these decision controls:

1. Keep D1, D2, D3, and subsequent IDs in order in `AGENTS.md`.
   Add each new decision after the last decision in that section.
   Do not change the IDs or their order.
   Do not delete a decision or use its ID again.
2. Do not change a recorded entry or its supporting files.
   Put corrections, reversals, status changes, and new evidence in a new entry.
   This includes spelling corrections and a label for a superseded decision.
3. Include `Amends: D<N>` or `Supersedes: D<N>` when a new decision changes a previous decision.
   Identify the points that change.
   Keep the other points in force.
   Read subsequent amendments before you use a previous entry.
4. Include the ID, recording date, title, selected behavior, and reason.
   Include applicable alternatives, costs, validation results, limits, and links.
   Identify planned checks and completed checks separately.
5. If more information is necessary, add a new file with the same decision ID.
   For example, use `reviews/decisions/D6-short-title.md` for D6.
   Connect the entry to that file when you record the decision.
   Do not change that file or its cited evidence after you record the decision.
6. Update goals, contracts, context links, and work instructions as the product changes.
   Do not change the decision history.
   Record important architecture changes and work-rule changes.
   Do not record each small implementation choice as a decision.

Do not replace recorded decisions with a summary or a new format.
If this task accidentally changed a record, restore its previous contents without other changes.
Put the selected change in a new decision.

## Apply the work rules

Use these defaults unless the user's requirements give a different choice:

- Read the behavior and applicable tests before a change.
- Complete the implementation and verification in the user task.
- Use clear names, small functions, and direct control flow.
- Add an abstraction only when the same responsibility occurs in multiple places or a new interface is necessary.
- Keep prose explanations in Markdown. Do not add prose comments to code, tests, examples, or documentation-site source.
- Do not change necessary compiler, build, or analysis directives without a technical reason. Do not add prose to these directives.
- If the user wants a prose comment, write that comment in STE.
- Change supported behavior only with user approval.
- Update callers, tests, examples, contracts, and migration instructions together when behavior changes.
- Keep formatting, lint, complexity, and coverage limits in their tool configuration files.
- Correct the cause of a failure. Do not change its check only to get a different result.
- Do not add suppressions for groups of rules.
- Select limits for this project. Do not copy limits from Artifacts without a project reason.
- Use tests of behavior that users can see and applicable failure cases.
- Do not add tests only to copy implementation or increase coverage.
- Use test resources that this task started or that the user gave to this task.
- Remove only those resources after the task.
- Keep sanitized evidence in a directory that cleanup does not remove.
- Do not change global developer configuration.
- Do not stop other services.
- Keep credentials out of command arguments, output, and evidence.
- Identify implementation, test results, measurements, assumptions, and claims without evidence separately.
- Use saved evidence only for its recorded source revision and environment.

## Prepare verification

Give the project one documented command for repository checks.
Use the selected tools, for example `make verify` or a package script.
If CI is in scope, use the same checks in CI.
Keep specified tool versions and limits in their configuration files.
Include document checks and the STE review for a repository that contains only documents.
Do not record test or coverage results without evidence for an empty implementation.

During development, start with checks for the changed behavior.
Then do the necessary repository checks.
Do more checks after a code change, a failure, or a remaining concern makes them necessary.

For a service, prepare a verification procedure through its public interfaces.
Start with a preflight that does not change data.
Include assertions about public results and cleanup.
Record the source revision, applicable worktree changes, environment, reproduction command, results, and limits.

Local mocks do not give evidence of hosted-service compatibility.
A small fixture does not give evidence of throughput.
Add a project verification skill only when an agent can use the procedure again.

For service work, put limits on resource use and obey cancellation.
For performance changes, measure workloads that use supported product operations and give the applicable costs.

After a push with user approval, examine CI for the commit that the push sent.
Wait for the applicable checks to complete.
Do an investigation before you connect a failure to the change.
Complete corrections in the user task until CI checks complete without failures.
If you cannot get remote results, record this limit.
This rule does not give user approval for a push.

For a large task, use a ticket when clear task limits help.
Include prerequisites, permitted paths, excluded paths, dependencies, public interfaces, rules, tests, completion criteria, and blocking conditions.
Use limits from the user task.
Give the cause of a scope conflict while other work continues.

## Complete the task

Do a check of generated links, commands, template fields, decision IDs, and decision references.
If the task changes a repository with files, compare decision records with their contents before this task.
Do the same comparison for supporting files and cited evidence.
Do a check for other changes and architecture assumptions from a different project.
Complete the STE review of all changed text and the response to the user.

Give the files made or changed, decisions added, completed checks, and remaining limits.
Give the STE review method and result.
If no push occurred, do not record remote CI as completed without evidence.

## Technical terms for this skill

These terms apply to this skill and its templates.
Use the software meanings of these terms.
Use category 19 of rule 1.5 for software nouns.
Use category 15 for document nouns and category 21 for nouns for rule governance.
Use category 2 of rule 1.12 for software verbs only when an approved general verb cannot give the correct meaning.

The standard defines its grammar terms.
Use those definitions for language review.
For other software terms, use their industry meanings in category 19.
Record a project-specific term when an industry term cannot give the correct meaning.

| Term | Part of speech | Meaning and category |
| --- | --- | --- |
| agent | Noun | Software that does tasks for a user. Category 19. |
| repository, repo | Noun | A Git project and its files. Use repository in prose. Keep `new-repo` as the skill name. Category 19. |
| commit | Noun | A Git record of file changes. Category 19. |
| push | Noun | A Git transfer to a remote repository. Category 19. |
| CI | Noun | Continuous integration, which does checks on a specified revision. Category 19. |
| software stack | Noun | The tools and technologies selected for a project. Category 19. |
| worktree | Noun | The files in a Git working directory. Category 19. |
| skill | Noun | Agent instructions in a `SKILL.md` file. Category 19. |
| template | Noun | A file with fields for project-specific text. Category 19. |
| metadata | Noun | Fields with data about a skill or a different software item. Category 19. |
| pull request | Noun | A proposal to add repository changes. Category 19. |
| code comment | Noun | Explanatory text in source code. Category 19. |
| documentation string | Noun | A source-code string that gives documentation for a software interface. Category 19. |
| decision register | Noun | The ordered decision entries in `AGENTS.md`. Category 15. |
| decision record | Noun | A recorded decision and its supporting files. Category 15. |
| STE review | Noun | An examination of text against the STE rules and dictionary. Category 15. |
| scope | Noun | The limits of a task. Category 21. |
| compliance | Noun | Conformity with a specified rule. Category 21. |
| import | Noun, verb | As a noun, a file inclusion. As a verb, read a file into a different tool. Categories 19 and 2. |
| copy | Noun, verb | As a noun, a duplicate file. As a verb, make a second file with the same contents. Categories 19 and 2. |
| delete | Verb | Remove stored data. Category 2. |
| restore | Verb | Put stored file contents back after a change. Category 2. |
| format | Noun, verb | As a noun, the data layout. As a verb, change that layout. Categories 19 and 2. |
| sanitize | Verb | Remove credentials and other private data from output. Category 2. |
| clone | Verb | Make a local copy of a Git repository. Category 2. |
| update | Verb | Change files or software to the selected revision. Category 2. |
| symlink | Noun | A filesystem entry that points to a different path. Category 19. |
| frontmatter | Noun | Metadata at the start of a document. Category 19. |

Add other necessary project terms to the technical-term table in the destination.
Do not copy this full table into a different product.
