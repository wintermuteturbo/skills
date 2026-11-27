# Types

Pick the type from the question the diagram answers. One diagram, one question.

| The question | Type | First line of the block | `render.mjs` draws it |
| --- | --- | --- | --- |
| What are the parts and how do they connect? | Flowchart with the three kinds of box | `flowchart LR` | Yes |
| What happens in which order, with branches or loops? | Flowchart | `flowchart TD` | Yes |
| Who sends what to whom, over time? | Sequence diagram | `sequenceDiagram` | Yes |
| Which states can a thing be in, and what moves it between them? | State diagram | `stateDiagram-v2` | Yes |
| Which records exist and how do they relate? | Entity-relationship diagram | `erDiagram` | Yes |
| Which classes exist and how do they relate? | Class diagram | `classDiagram` | Yes |

Some content looks like a diagram and is not one:

| The content is | Use |
| --- | --- |
| Steps in a fixed order with no branch | A numbered list |
| Items compared on the same points | A table |
| Parents and children with no cross links | An indented list or a directory tree |
| A reason, a trade-off or a caveat | Prose |

Mermaid has more types, such as Gantt charts, timelines and mind maps. They draw wherever standard Mermaid runs, and the render script cannot draw them: deliver the block alone.

## One zoom level

A parts diagram shows one level and never mixes them:

- systems and the people who use them, or
- the deployable parts inside one system, or
- the components inside one part.

A reader who needs two levels gets two diagrams: the overview first, then the detail.

## Direction

- Many boxes side by side at one level: left to right, `flowchart LR`.
- A deep chain of steps: top down, `flowchart TD`.

Keep the one direction through the whole diagram. An arrow that runs back against it should be a real loop in the system.

## Limits

| Type | Limit | Checked by `check.py` |
| --- | --- | --- |
| Flowchart | 9 boxes and 12 arrows | Yes |
| Every other type | None tested yet | No |

Over the limit, split by question or by zoom level. For the types without a tested limit, apply the remove test, and split when one question has become two.
