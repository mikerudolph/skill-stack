# Work on {{PROJECT_NAME}}

Read [GOALS.md](GOALS.md) for the product purpose.
Use this file to find the applicable implementation and checks.
Keep each explanation in its applicable document.
Use links to that document instead of duplicate explanations.

## Find the applicable context

| Task | Start here |
| --- | --- |
| Find the product purpose and scope | [GOALS.md](GOALS.md) |
| Prepare or operate the project | [README.md](README.md) |
| Change implementation or contracts | {{IMPLEMENTATION_AND_CONTRACT_LINKS}} |
| Do repository checks | {{VERIFICATION_CONFIG_LINK}} |

Saved reviews and evidence apply to a specified revision and test run.
Read code and contracts for the behavior at the applicable revision.

## Decision register

Keep D1, D2, D3, and subsequent IDs in order here.
Add each new entry after the last decision, before `Work rules`.
Do not change the IDs or their order.
Do not delete a decision or use its ID again.

Do not change a recorded decision or its supporting files.
Put corrections, reversals, status changes, and new evidence in a new decision.
This includes spelling corrections and labels for superseded decisions.
Include `Supersedes: D<N>` or `Amends: D<N>` when the new entry changes a previous decision.
Identify the points that change.
Keep the other points in force.

Each entry gives its ID, recording date, title, selected behavior, and reason.
Include applicable alternatives, costs, validation results, limits, and links.
Identify planned checks and completed checks separately.
If more information is necessary, add a supporting file with the same ID.
Connect the entry to that file when you record it.
Do not change the supporting file or its cited evidence after that time.

The initial entries record the selected work rules on {{RECORDING_DATE}}.
This is the recording date, not the date of a previous choice.

### D1 ({{RECORDING_DATE}}): Add decisions to change decisions

Do not change recorded decision entries or their supporting files.
Add a new entry for corrections, reversals, and changes.
Identify the points that the new entry changes.
Keep the other points in force.
This method keeps the reasons for previous choices available for review.
Read subsequent amendments before you use a previous decision.

### D2 ({{RECORDING_DATE}}): Use different documents for goals, contracts, and decision history

`GOALS.md` gives the product purpose and scope.
`AGENTS.md` gives context links, work rules, language rules, verification commands, and the decision register.
The README and contract documents give setup and behavior.
Update these documents as the product changes.
Do not change the recorded decisions.
This method keeps instructions applicable and decision history available.

### D3 ({{RECORDING_DATE}}): Keep prose explanations in documents

Do not write prose comments in implementation files, tests, examples, or documentation-site source.
Use names and structure to make code clear.
Put explanations in Markdown documents.
Keep necessary compiler, build, and analysis directives without added prose.
This method keeps explanations in their applicable documents.

### D4 ({{RECORDING_DATE}}): Use verification evidence for completion claims

Use the documented repository checks and their configured limits.
Use tests of behavior that users can see and applicable failure cases.
Do checks through public interfaces when the product promise makes them necessary.
After a push with user approval, examine CI for the commit that the push sent.
Wait for the applicable checks to complete.

Do an investigation of failures.
Complete corrections with user approval until CI checks complete without failures.

Identify local results, remote results, measurements, and claims without evidence separately.
This method connects completion claims to evidence and its limits.

### D5 ({{RECORDING_DATE}}): Use ASD-STE100 for project text

Use ASD-STE100 Issue 9, dated 2025-01-15, for all new or changed human-readable project text.
This includes decisions, permitted comments, documentation strings, user messages, commit messages, issues, pull requests, reviews, and agent responses.
Use the standard rules, dictionary, and applicable technical-term categories.
Complete an STE review before delivery of the text.
Do not change recorded decisions, their evidence, or necessary literal values.
Add a new decision for a subsequent language-rule change.

This rule gives the project one language standard for documents, software text, and collaboration.

## Work rules

1. Read behavior and applicable tests before a change.
   Do not change other user work.
   Complete the implementation and verification in the user task.
2. Use clear names, small functions, and direct control flow.
   Add abstractions when the same responsibility occurs in multiple places or a new interface is necessary.
3. Obey D3 for code comments.
   If the user wants a prose comment, write that comment in STE.
4. Keep formatting, lint, complexity, and coverage limits in their tool configuration files.
   Correct the cause of a failure.
   Do not change its check only to get a different result.
   Do not add suppressions for groups of rules.
5. Change supported behavior only with user approval.
   Update callers, tests, examples, contracts, and migration instructions together when behavior changes.
6. Make public documentation and configuration descriptions agree with implementation.
   Identify targets, limits, and work that is not in the selected scope.
7. Use test resources that this task started or that the user gave to this task.
   Remove only those resources.
   Do not change global developer configuration.
   Do not stop other services.
   Keep credentials out of command arguments, output, and evidence.
8. Record the source revision, applicable worktree changes, environment, and reproduction command with the evidence.
   Keep sanitized results in a directory that cleanup does not remove.
   Identify target, authentication, product, evidence, and cleanup failures separately when applicable.
9. Give the change, completed checks, and remaining limits.
   Identify implemented behavior, observations, measurements, and assumptions separately.

## Language rules

Read [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) before you write project text or do an STE review.
Use the standard for all new or changed human-readable text.
This includes agent responses and collaboration that is not in repository files.
This includes all items in D5 and prose from project-controlled generators.
Keep necessary commands, paths, identifiers, protocol values, legal text, and quotations without changes.
Use STE for their explanations and approved terms for new identifiers.

Complete an STE review of changed text before task completion.
Record the issue, review method, result, and remaining terms or rule questions.
If the repository has an STE checker, use it with the repository checks.
Also do an STE review of meaning and technical terms.
A checker result is not sufficient evidence of full STE compliance.

If the standard or review is not available, record `STE review: not completed`.
Give the cause.

Apply the language rule to new decisions and subsequent text.
Do not change a previous decision or its supporting files for language corrections.
Add a new decision for the correction.

### Technical terms

{{PROJECT_TECHNICAL_TERMS}}

Give each term, its meaning, part of speech, and applicable STE rule category.
Use one term for each concept.
Use technical terms only in their recorded technical context.
Do not put general words that STE rejects in this table.

## Verification

During development, start with checks for the changed behavior.
Use regression tests for changes to public results and applicable failure cases.
Do not add tests only to copy implementation or increase coverage.

Before task completion, use:

```sh
{{VERIFY_COMMAND}}
```

{{VERIFICATION_CONFIG_LINK}} gives the specified checks, tool versions, and limits.
Keep those values in that file.
{{ADDITIONAL_VERIFICATION_GUIDANCE}}

Complete the STE review of repository text and collaboration text.
Do more checks after a change, a failure, or a remaining concern makes them necessary.
If a necessary check cannot operate, give the cause and the completed checks.
Do not record a check as completed if it could not operate.

After a push with user approval, examine CI for the commit that the push sent.
Wait for the applicable checks to complete.
If you cannot get remote results, record this limit.
This rule does not give user approval for a push.

## Add the next decision

Read the register, supporting records, and subsequent amendments before a change to a recorded decision.
Add the next new D-number in the register above.
Include the recording date and applicable `Amends:` or `Supersedes:` references.
Give the problem, selected behavior, reason, alternatives, costs, verification results, and remaining limits.
Use STE for the new entry.

If more information is necessary, add a file such as `reviews/decisions/D6-short-title.md`.
Connect the new decision to the file when you record the decision.
Do not change previous decision files or their saved evidence.
Update documentation and implementation separately.

Record important architecture changes and work-rule changes.
Do not record each small implementation choice as a decision.
Do not put proposals or open choices in the decision register.
