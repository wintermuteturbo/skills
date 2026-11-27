# Destinations

What to deliver depends on whether the destination draws Mermaid itself. The source goes everywhere; a picture goes only where nothing draws the source.

| Destination | People see | Agents read | Deliver |
| --- | --- | --- | --- |
| GitHub Markdown: a README, a doc, a pull request, an issue | The block, drawn by GitHub | The block | The Mermaid block in a `mermaid` code fence, then the key |
| Confluence | An image | The source under the image | The SVG as an image with the title as its caption, then the Mermaid source in a collapsed block under it, then the key |
| Claude artifact doc | The block as the doc draws it, or the doc tool's own diagram | The doc text | The Mermaid block, or the doc tool's diagram when it has one |
| Chat or a terminal | The block as text | The block | The Mermaid block in a code fence. For a reader who cannot draw it, add the text drawing from `render.mjs --ascii` |
| Anything that draws neither Mermaid nor images | Text | Text | A table or a list in place of the diagram |

## Rules for a picture

- **The SVG is made, never edited.** Change the source and run `node scripts/render.mjs` again.
- **The source travels with the picture.** Under the image, in a collapsed block, or as a `.mmd` file beside the `.svg` with the same name.
- **The caption is the title.** The render script prints it. Use it as the alt text too.
- **The key and any exact value stay in the text.** A reader who gets only the text must lose nothing a reader of the picture has.

## Not yet checked

These were unknown when this version was written. Where you can look at the result in the destination, do, and tell the user what you saw.

| Destination | Unknown | If it goes wrong |
| --- | --- | --- |
| GitHub | Which Mermaid version it runs, and whether that version has the ELK layout | The diagram should still draw, with slanted arrows. If it does not draw at all, remove the `layout: elk` line first |
| GitHub | How the house colours look in dark mode | Report it; do not change the colours for one diagram |
| GitHub and Confluence | Whether the SVG shows correctly as an image. It uses CSS variables and `color-mix()`; a browser drew it correctly, and one image converter drew black boxes | Deliver the Mermaid block alone and say why |
| Confluence | Whether the site has a Mermaid app | With one, deliver the block alone and skip the image |
| Claude artifact docs | How they draw a Mermaid block | Use the doc tool's own diagram |
