# Sources

Where each rule comes from, for people who want to check or argue. You don't need this file to draw.

## Status of this version

This is version 0.2.0, still a draft. Its rules are candidates:

- A research pass on what makes a software diagram easy to read has not been done yet.
- The skill has not been benchmarked. The plan is three tests: a person ranking drawings, a diagram test for agents, and cost.
- Tested so far, on 23 to 25 November 2026: the house style drawn by Mermaid 11.16 and by beautiful-mermaid 1.1.3 on two diagrams of 5 and 14 boxes, the two scripts on those diagrams, and numbered arrows and phase views in both renderers.
- Changed from 0.1.0: numbered arrows, phase views and the `compatibility` line.

## Why Mermaid text is the source

| Finding | Source |
| --- | --- |
| A coding agent's judged code quality rose once it was given a written architecture, and the format mattered little to the strongest model. Three trials per cell, so a hint and not proof. | [Architecture as Capability Equalizer for Coding Agents](https://arxiv.org/pdf/2608.21747), 2026 |
| On architecture diagrams given as images, the best of 11 vision models answered 70% of the questions. Long, overlapping and diagonal arrows caused frequent errors. | [Benchmarking and Evaluating VLMs for Software Architecture Diagram Understanding](https://arxiv.org/html/2604.04009v1), 2026 |
| Vision models read the boxes in a diagram image well and the arrows poorly, and accuracy on relations drops as diagrams grow. | [Do Vision-Language Models Really Understand Visual Language?](https://arxiv.org/pdf/2410.00193v2), 2024 |
| Questions about a diagram's structure were answered more accurately from a text form than from its image. A proof of concept with no numbers. | [Overcoming Vision Language Model Challenges in Diagram Understanding](https://arxiv.org/abs/2502.04389), 2025 |

In our own comparison a hand-drawn SVG took nine times the source of the Mermaid block for the same five-part diagram.

## The house style

One diagram was drawn four ways on 23 November 2026 and ranked by the skill's owner: SVG drawn by hand first, Mermaid with the house style and ELK second, the house style with the default layout a close third, and default Mermaid last. The house style with ELK is the best look that keeps Mermaid as the source.

[ELK](https://eclipse.dev/elk/reference/algorithms/org-eclipse-elk-layered.html) is the Eclipse Layout Kernel, an open-source layout engine that arranges boxes in layers, reorders them to reduce crossings and can run arrows at right angles.

## The rules

| Rule | From |
| --- | --- |
| Never ship the default theme; one theme with a few kinds of box; render and look before delivering | [github-mermaid-diagrams](https://skills.sh/ekroon/agent-skills/github-mermaid-diagrams) and [mermaid-diagram](https://tessl.io/registry/skills/github/mgranberry/mermaid-diagram-skill/mermaid-diagram), two public skills |
| The remove test; at most 9 boxes and 12 arrows; a key that covers every kind used and nothing more; a check script | [diagram-design](https://github.com/cathrynlavery/diagram-design), a public skill, MIT |
| One question and one zoom level per diagram; a label on every arrow; the names the code uses | The `reader-first-docs` skill's figures reference, which takes its zoom levels from the C4 model |
| The key as a sentence, not a drawn box | Our test: a drawn key took a third of the picture |
| Numbered arrows, and one view per phase of a flow | [system-flow-diagrams](https://github.com/ClarkOhlenbusch/system-flow-diagrams), a public skill, MIT, which plays a flow one phase at a time in an interactive page. The Mermaid way of doing it here is ours. Its hand-set positions and its need for a network were not taken. |
| One idea per diagram, labelled lines, a key, never colour alone, text sources kept beside the docs | *Docs for Developers*, 2nd edition, 2026, chapter 6, which agrees with the rules above |

## The renderer

[beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid), MIT, version 1.1.3: it drew our diagrams in 0.1 to 0.2 seconds with no browser, where Mermaid's own command-line renderer took about 2 seconds and needs a headless browser.
