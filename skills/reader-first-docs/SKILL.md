---
name: reader-first-docs
description: Write or revise software documentation so that one named reader can use it fast. Covers design docs, RFCs, decision records (ADRs), READMEs, how-to guides, runbooks, reference, architecture overviews and "how this works" explanations. Use whenever the user asks to write up, document, explain or describe a system, feature, decision or change for someone else to read, to bring docs up to date after a change, and whenever a doc is called too long, a wall of text, unclear, or in need of a diagram, even if nobody says "documentation". Gives a shared vocabulary (reader, kind, brief, lead, budget, figure, facts) and a brief, draft, cut, test loop whose output works for people and for coding agents.
license: MIT OR Apache-2.0
---

# Reader-first docs

Write the shortest doc that lets one named **reader** do one thing, then test it on a reader who was not there.

Docs fail in one way more than any other: the writer records what they know instead of what the reader needs. The doc grows, the point sinks, and content that should be a picture becomes paragraphs. Better sentences don't fix that. Deciding who reads and why, before writing, does.

## Glossary

Use these terms exactly, in your planning and when you discuss the doc with the user. Shared words are what let a writer, a reviewer and an agent hold a doc to the same standard.

**Reader**: the one person or agent the doc is for, named by role and by what they already know: "a backend engineer new to this service", "a coding agent about to change the retry logic". One doc has one reader. _Avoid_: audience, users, stakeholders. Plurals hide the choice.

**Kind**: the form that fits why the reader opens the doc. A closed set: tutorial (to learn), how-to (to do a task), reference (to look up), explanation (to understand), proposal (to decide), decision record (to know what was decided), landing page (to find their way). One doc, one kind. A doc doing two kinds' work is the usual cause of length. The first four are Diátaxis.

**Brief**: six lines written before the draft. It names the reader and the kind, then adds:
- **Outcome**: one sentence, "After reading, the reader can …". Every line of the doc is judged against it.
- **Reader questions**: the three to seven questions this reader would ask. The doc exists to answer them.
- **Budget**: the most words the doc may have, from the kind (see [references/kinds.md](references/kinds.md)). It is a ceiling, not a size to fill: the doc ends when the reader questions are answered, and most good docs end well under it. Over budget means cut or split, never squeeze.
- **Unknowns**: what the doc needs and you could not find. They are reported, never guessed.

**Lead**: the opening lines, which give the answer: the decision asked for, what the thing is, the result. A reader who stops after the lead leaves with the point. When the doc asks its reader for something, the first sentence is the request: what you need, from whom and by when. When only some people need the doc, the lead says who. _Avoid_: introduction, background, overview. Those name a section that delays the point.

**Layer**: lead, then body, then depth. Each layer is complete for the readers who stop there. Depth is what few readers need; it goes last or in a linked doc.

**Standalone section**: a section that still makes sense to someone who lands on it from search, or to an agent handed that section alone. Its heading says what it holds in the words the reader would search for, its first sentence is its point and names its subject in full, and it never says "as mentioned above".

**Figure**: any form that isn't prose: a diagram, a table, a numbered list, a code sample. Content with a **shape** (a sequence, parts and connections, states, a comparison, a hierarchy) gets the figure that matches. Prose is for reasons.

**Takeaway**: the one sentence after a figure that says what to see in it.

**Facts**: the exact values a reader will act on: names, paths, commands, limits, versions, invariants. Copied from the source, stated in words, never only inside a figure.

**Cut test**: delete the sentence. If the reader can still reach the outcome, it stays deleted.

**Reader test**: giving the finished doc, and nothing else, to a fresh reader and checking it against the reader questions.

## The loop

1. **Brief.** Write the six lines first and show them to the user above the doc, not inside it. If the request doesn't name the reader, pick the likeliest one and say so. Ask only when two plausible readers would need different kinds of doc. A wrong reader makes the whole doc wrong, and the brief is the cheapest place to catch it.

   ```
   Reader:    on-call engineer who knows the service, not this job
   Kind:      how-to
   Outcome:   After reading, the reader can re-run a failed export safely.
   Questions: When is it safe? What command? How do I know it worked? What if it fails again?
   Budget:    400 words
   Unknowns:  none yet
   ```

2. **Gather.** Read the code, the thread, the existing docs. Find the doc's home first: when a doc already owns this topic, update it and do not write a second one, and give a new doc the section order its sibling docs use. Collect facts with where each came from. Look hardest for what the reader cannot get by reading the code: why it is this way, what was rejected, what must stay true. Write down what you could not find under Unknowns. Never fill a gap with plausible detail: a wrong doc is worse than a missing one, and an agent will act on it without checking.

3. **Shape.** Take the skeleton for the kind from [references/kinds.md](references/kinds.md). Then scan the material for shapes and choose figures with [references/figures.md](references/figures.md). Three "then"s in a paragraph is a sequence. Four components that call each other are a diagram. Two options judged on the same points are a table.

4. **Draft.** Write the lead first; if you can't, the brief is wrong, so go back. Then the body as standalone sections, with headings that state content ("Retries stop after five attempts") in place of labels ("Details"). Use one name per thing, the name the code uses; when the reader would search for another word, give both once ("the `jobs` table, the queue"). State facts exactly. Keep bold for the one or two things the reader must not miss, such as the ask or a warning: where everything is bold, the reader reads the bold and skips the rest.

5. **Check and cut.** Check before you cut: hold every command, name, number and limit against the source it came from, and say which version or environment the doc is true for. Then hold each section against the reader questions: a section that answers none of them goes to the depth layer or goes away, however true it is. Then apply the cut test line by line. What usually goes: how the team got here, anything the code or the README already says, hedges, sentences that announce ("This section describes …"), the second example, and anything written for a different reader. Last, count words (`wc -w`). Being under the budget proves nothing, and a draft that lands just under it was probably written up to it, so cut once more. Over budget after that? Split by kind or by reader into two docs that link to each other.

6. **Reader test.** If you can start a subagent, give it only the doc, one line describing the reader, and the reader questions. Ask it to answer each question from the doc alone and say where it found the answer, to answer "not in the doc" when it isn't, and to name what it had to read twice. If you can't, do two cold checks yourself: read only the lead and state the outcome; then read only the headings and takeaways and name the section that answers each question. Fix what failed, and take out as many words as each fix adds: writers asked to improve a text add to it. Then report.

Finish with a report to the user of 150 words at most, plus the brief. Lead with what they must check or decide before using the doc, then give the word count, the reader test result and the unknowns as one line each, and for a new doc name the index or README that should link to it. The user is a busy reader too: a report longer than the doc has lost them. Unknowns the reader needs also appear in the doc as open questions; ones only the user needs stay in the report.

## One source, two readers

Most docs are now read by a person and by an agent. They want nearly the same thing, and where they differ the rule is to never make one depend on the other's form.

- **A person looks before reading; an agent reads only text.** Write figures as text the page renders: Mermaid, Markdown tables, code blocks. An image alone gives an agent nothing but its alt text. Follow every figure with its takeaway, and repeat in words any fact the figure carries.
- **An agent may get one section with none of the rest.** That's why sections stand alone and headings state content.
- **An agent pays for every token and gets less reliable as input grows; a person just stops reading.** That's why there's a budget, and why you don't restate what the code or another doc already says. Link to it.
- **An agent treats two words as two things.** One name per thing.
- **An agent acts on what it reads without asking.** Put a "Last checked" date and what it was checked against on anything that can go stale, and delete what you can't keep current.

When the reader is an agent alone (AGENTS.md, a context file, another skill), write only what it cannot work out from the repository: exact commands, the tool to use, constraints, conventions that differ from the default. A codebase overview costs it tokens and doesn't help it find anything.

## Revising a doc someone else wrote

Start by recovering the brief from the doc itself. If you can't tell who the reader is or what they can do afterwards, that is the main finding; say it before changing anything. Then run the loop from step 3. Never drop content silently: list what you cut and where it went (depth, another doc, or gone because the code already says it).

Signs a doc has lost its reader:

- It opens with history or background.
- Headings are labels: "Overview", "Introduction", "Details", "Notes".
- A paragraph walks through steps or components in sentences.
- One thing has two names, or two things share one.
- A figure has no takeaway, or a takeaway has no figure it needed.
- It teaches, instructs and records decisions in the same breath.

## Updating docs after a change

When the task is a change to the code, find the docs the change makes wrong before writing anything new. Search the docs for the names, commands, limits and paths the change touches. Update each doc where it stands and in its own kind. Mark what the change retires with what replaces it and from when, and delete what is now false. Report the docs you changed and the ones you could not check.

## A small example

Before, 61 words, from a design doc:

> The export service was originally written in 2022 and has gone through several iterations. Currently, when an export is requested, the API first validates the request and then writes a job row, after which the worker picks it up, generates the file, uploads it to storage and finally sends the user an email with a link that expires after 24 hours.

After, for a reader who must debug a stuck export:

> An export passes through four steps, and a stuck one is waiting at the step its job row names.
>
> 1. The API validates the request.
> 2. The API writes a job row (`export_jobs.status = queued`).
> 3. The worker generates the file and uploads it to storage.
> 4. The worker emails a link that expires after 24 hours.

The history went (cut test: this reader doesn't need it). The sequence became a numbered list. The lead now says what the reader can do with the list, and one fact gained its exact name.

## Reference files

- [references/kinds.md](references/kinds.md): for each kind, what the lead holds, the skeleton, what to leave out, and the budget. Read it at step 3.
- [references/figures.md](references/figures.md): which figure fits which shape, and the rules for diagrams, tables and code samples. Read it when the material has a shape.
- [references/sources.md](references/sources.md): where each rule comes from. For people who want to check or argue; you don't need it to write.
