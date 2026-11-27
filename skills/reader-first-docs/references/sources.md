# Sources

Where each rule in this skill comes from, for people who want to check a rule or argue with it. An agent writing a doc doesn't need this file.

| Rule in the skill | Source |
| --- | --- |
| One reader; judge every line from their side | Clements et al., *Documenting Software Architectures*, rule 1 of the seven rules for sound documentation. Winters, Manshreck and Wright, *Software Engineering at Google*, chapter 10. Larry McEnerney, "The Craft of Writing Effectively". |
| Kinds, and one kind per doc | Daniele Procida, Diátaxis (tutorial, how-to, reference, explanation). *Software Engineering at Google*, chapter 10 (one purpose per document). Proposal and decision record are added here for engineering work. |
| Lead: answer first | Barbara Minto, *The Pyramid Principle*. Nielsen Norman Group, "Concise, Scannable and Objective" (inverted pyramid). Malte Ubl, "Design Docs at Google". |
| Budget and the cut test | Carroll, *The Nurnberg Funnel* (minimalism). IBM, *Developing Quality Technical Information* (completeness is enough and only enough). Rogers and Lasky-Fink, *Writing for Busy Readers*. Nielsen Norman Group measured 58% better usability at half the word count. |
| Budget numbers | Ubl gives 1 to 3 pages for a small design doc and 10 to 20 for a large project. Michael Nygard gives one or two pages for a decision record. The other numbers are this skill's defaults and are meant to be tuned against its benchmark. |
| Standalone sections | Mark Baker, *Every Page Is Page One*. Write the Docs, documentation principles (accept some repetition). n8n, "Agent-friendly docs". |
| Shape decides the figure | Larkin and Simon, "Why a Diagram is (Sometimes) Worth Ten Thousand Words", 1987. Richard Mayer, *Multimedia Learning* (multimedia and coherence principles). IBM (visual effectiveness). |
| Diagram rules: title, one zoom level, labelled arrows | Simon Brown, the C4 model and its notation guidance. Clements, rule 3 (explain your notation). |
| Facts stated exactly, in words | IBM (accuracy, concreteness). Julia Evans, "Patterns in confusing explanations". n8n (instructions live in text, not images). |
| One name per thing | Clements, rule 3 (avoid ambiguity). Write the Docs (consistent). |
| Write what the code cannot say | Clements, rule 5 (record rationale). John Ousterhout, *A Philosophy of Software Design*. Gloaguen et al., "Evaluating AGENTS.md", 2026: context files that restate the repository raised agent cost by about 20% without raising success. |
| Proposal skeleton | Malte Ubl, "Design Docs at Google". |
| Decision record skeleton | Michael Nygard, "Documenting Architecture Decisions", 2011. |
| How-to: recognise and recover from errors | van der Meij and Carroll, minimalism principle 3. |
| Never guess; date what can go stale | Write the Docs (incorrect is worse than missing). *Software Engineering at Google* (owners and freshness dates). |
| Reader test | Clements, rule 7 (review for fitness of purpose). Anthropic's doc-coauthoring skill (testing a doc on a fresh agent). SWD-Bench, 2026, arXiv 2604.06793 (judge a doc by what a reader can do with it). |
| Keep the skill itself short | Li et al., SkillsBench, 2026: focused skills beat comprehensive ones. |
| Search words in headings; both names once; the doc's home | Bhatti et al., *Docs for Developers*, 2nd edition, 2026, chapters 9 and 10. Two public skills say the same: blockmatic's technical-writing (edit for retrieval, find the page that owns the topic). |
| Check before the cut, accuracy first | *Docs for Developers*, chapter 4 (edit in separate passes). dsebastien's technical-documentation skill. |
| Title form by kind | *Docs for Developers*, chapter 3. |
| How-to: follow the steps before it ships, warnings before the step, errors quoted exactly, values to replace | *Docs for Developers*, chapters 1, 3, 4, 5 and 7 (friction logs, callouts, code samples, testing before release). |
| Updating docs after a change | *Docs for Developers*, chapter 11 (which docs a change affects, deprecation notes). |
| Proposal: the request in the first sentence, four parts first, options and questions for the reader under the lead, who reviews what | Rogers and Lasky-Fink, *Writing for Busy Readers*: fewer ideas and requests, order by priority, say who should care, make responding easy. Read here through a third-party summary, so the principles are sound and the wording of these rules is this skill's own. The four-part default also follows tech-leads-club's design-doc skill, which scales sections to the size of the project. |
| Bold only for what must not be missed; fixes that do not add words | *Writing for Busy Readers*, on formatting and on the habit of adding when editing, through the same summary. |
| The request opens the lead | This skill's third benchmark run, 25 November 2026: when the request closed the lead, readers of the first 150 words answered fewer questions right. |
