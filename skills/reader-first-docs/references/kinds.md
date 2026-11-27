# Kinds

Each kind serves one reason for opening a doc, so each has its own lead, skeleton, things to leave out and budget. Pick one kind per doc. When the material needs two, write two docs and link them.

| Kind | The reader wants to | The title is | Budget in words |
| --- | --- | --- | --- |
| [Proposal](#proposal) (design doc, RFC) | decide, or review a decision before it is made | what would change: "Scheduled exports through one hourly job" | 1,500 for a feature; 5,000 for a system |
| [Decision record](#decision-record) (ADR) | know later what was decided and why | the decision as a sentence | 400 |
| [Explanation](#explanation) (how it works, architecture overview) | understand a system well enough to change it | a noun phrase: "How invoice reminders work" | 1,200 |
| [How-to](#how-to) (guide, runbook) | get one task done now | the task as a verb phrase: "Rotate the signing key" | 600, and 12 steps |
| [Reference](#reference) | look up one fact | the name of the thing | none; one uniform entry per thing |
| [Tutorial](#tutorial) | learn by doing | what the learner builds | what a learner finishes in 30 minutes |
| [Landing page](#landing-page) (README, index) | find out what this is and where to go | the name of the project | 400 before the links |

The budgets are ceilings for a doc with no other constraint, not sizes to reach. A budget the user gives replaces them. Count with `wc -w` on the whole file.

A skeleton gives the order of the parts, not a form to fill in. Keep the parts this reader needs to reach the outcome and leave the rest out: a reviewer asked to approve one change does not need every risk and every non-goal.

## Proposal

**Lead:** open with the request in one sentence: the decision you need, from whom and by when, with the option you recommend. Then what you propose, the main trade-off, and what happens if nobody answers. Four sentences at most, above everything but the status line. The other options go below the lead, not in it.

**Skeleton:** build it from four parts, and add another only when a reader question needs it. A proposal that fills every part below is longer than its reader needs.

The four parts every proposal has:

1. Status line: one short line with status, author and date. Who decides and by when go in the lead.
2. Lead, opening with the request.
3. Design. Open with one diagram that places the change among the systems the reader already knows, and its takeaway. Then cover the parts where a real choice was made, each with its trade-off.
4. Alternatives considered: a table of options against the criteria that decided it, and one line on why each lost.

Parts to add when a reader question needs them:

- Options and questions for the reader, directly under the lead: when the request has more than one option, the options by name with the recommended one first; then anything else this reader must answer, each as a choice between named options.
- Reviewers, when other people review it too: one line under the lead that sends each to the section that is theirs: "Security: read 'Bucket access'".
- Context: only the facts this reader lacks. No history of the discussion.
- Goals and non-goals, as bullets. A non-goal is something that could reasonably have been a goal and was left out on purpose; "must not crash" is not one.
- Risks that apply here: security, privacy, data migration, rollout, observability. Skip the ones that don't.
- Open questions that someone else will settle, each with an owner.
- Depth: schemas, long examples, benchmarks. Linked or appended.

**Leave out:** implementation steps that involve no choice. If the whole doc would be that, there is nothing to decide and no proposal to write; say so. Over 5,000 words, split it into one proposal per decision.

**After the decision:** record it as a decision record and mark the proposal's status. A proposal describes a moment; it isn't kept current.

## Decision record

**Lead:** the decision as a full sentence in the title: "Use Postgres advisory locks for the job queue".

**Skeleton:**

1. Title: number and decision.
2. Status: proposed, accepted, or superseded by a link.
3. Context: the forces at play, stated as facts.
4. Decision: "We will …".
5. Consequences: what becomes easier, what becomes harder, what we now have to do.
6. Rejected: each alternative in one line with its reason.

**Leave out:** how to implement it, and more than one decision. An accepted record is never edited; a new record supersedes it.

## Explanation

Use this for "document the existing solution".

**Lead:** what the system is and does in two or three sentences, and when a reader would need this doc.

**Skeleton:**

1. Lead.
2. The map: one diagram of the parts and how they connect, with its takeaway.
3. One request, start to finish: a sequence diagram or numbered steps following a real example through the parts.
4. Why it is this way: the decisions and constraints that shaped it, linked to their decision records.
5. What must stay true: invariants, limits and known sharp edges, as facts.
6. Where to look: a table of path against what lives there.

**Leave out:** a walk through the code line by line; the reader has the code. Write what the code cannot say: the map, the why, the invariants. Leave task steps to a how-to and exhaustive detail to reference.

## How-to

**Lead:** the title is the task ("Rotate the signing key"). Under it: what this does, when to use it and when not, how long it takes, and what could go wrong.

**Skeleton:**

1. Lead.
2. Before you start: access, tools and state the reader needs, and where to get each. A reader who lacks one should find out here, not at step six.
3. Numbered steps. One action per step, the command in a code block, then what the reader should see. A warning goes before the step it protects, and only for harm, lost data or what cannot be undone.
4. Check it worked.
5. If it fails: the errors a reader is likely to hit, each quoted exactly as it appears so a search finds it, with its fix or its way back.

**Before it ships:** follow the steps yourself from the reader's starting state, and note where what happens differs from what the doc says. Fix the doc. When the fault is in the product, tell the user and do not document around it. If you could not run the steps, say so in the report.

**Leave out:** why the system works this way (link the explanation), alternatives, and options most readers won't use. Over 12 steps, split into two tasks.

## Reference

**Lead:** one line per entry that says what the thing is or does, starting with a verb for functions and commands.

**Skeleton:** the same for every entry, in the order of the thing documented: name or signature, the one line, parameters as a table (name, type, default, meaning), what it returns, errors, one minimal example. Mirror the structure of the code or the product, so a reader who knows one can find their way in the other.

**Leave out:** teaching, opinion and narrative. Generate what can be generated from the source so it can't drift.

## Tutorial

**Lead:** what the learner will have built or done by the end, and what they need before starting.

**Skeleton:** a lesson. Numbered steps the learner performs, each with a visible result, starting from nothing and reaching something that works early. Explain only what the next step needs. Run it from nothing before it ships, as for a how-to.

**Leave out:** choices, alternatives and background. A learner who must decide is no longer learning the thing in front of them. Link the explanation at the end.

## Landing page

**Lead:** what this is, in one sentence a newcomer understands, and who it is for.

**Skeleton:**

1. Lead.
2. The shortest path to a working result: install, then one command or snippet, then what the reader should see.
3. Where to go next: links grouped by what the reader wants to do.

**Leave out:** anything a link can hold. A landing page directs traffic; it doesn't store content.
