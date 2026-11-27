#!/usr/bin/env node
// Render one Mermaid diagram to an SVG picture, in the house colours.
//
// Usage:
//   node render.mjs <file.mmd | file.md> [--block N] [--out file.svg]
//   node render.mjs <file.mmd | file.md> [--block N] --ascii
//
// A Markdown file is searched for ```mermaid blocks; --block picks one (default 1).
// Without --out the picture is written beside the input: diagram.mmd -> diagram.svg,
// doc.md -> doc-1.svg. With --ascii a text drawing is printed and no file is written.
//
// Needs Node 18 or later and the npm package `beautiful-mermaid`, found from this
// script's folder or from the folder you run it in. The script installs nothing.
//
// Exit codes: 0 done, 1 bad arguments or unreadable input, 2 the diagram could
// not be drawn, 3 beautiful-mermaid is not installed.
//
// What the script changes on the way:
//   - the header block (--- ... ---) is removed, because the renderer rejects it;
//     its title is kept as the SVG's <title> and printed for the caption
//   - the renderer's web-font import is removed, so the picture never calls out
//     to the network; text falls back to the reader's system font

import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, dirname, extname, join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const HOUSE = {
  bg: '#ffffff',
  fg: '#1f2328',
  line: '#6e7781',
  accent: '#0969da',
  muted: '#57606a',
  surface: '#f6f8fa',
  border: '#8c959f',
};

function fail(code, message) {
  process.stderr.write(message + '\n');
  process.exit(code);
}

function parseArgs(argv) {
  const args = { input: null, block: 1, out: null, ascii: false };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--ascii') args.ascii = true;
    else if (arg === '--block') args.block = Number(argv[(i += 1)]);
    else if (arg === '--out') args.out = argv[(i += 1)];
    else if (arg.startsWith('--')) fail(1, `unknown option ${arg}`);
    else if (args.input === null) args.input = arg;
    else fail(1, 'give one input file');
  }
  if (args.input === null) fail(1, 'usage: node render.mjs <file.mmd | file.md> [--block N] [--out file.svg] [--ascii]');
  if (!Number.isInteger(args.block) || args.block < 1) fail(1, '--block takes a number, 1 or more');
  if (args.out === undefined) fail(1, '--out takes a file path');
  return args;
}

function mermaidBlocks(markdown) {
  const blocks = [];
  let current = null;
  for (const line of markdown.split('\n')) {
    if (current === null) {
      if (/^\s*```+\s*mermaid\s*$/.test(line)) current = [];
    } else if (/^\s*```+\s*$/.test(line)) {
      blocks.push(current.join('\n') + '\n');
      current = null;
    } else {
      current.push(line);
    }
  }
  return blocks;
}

// The package's entry file, looked for in node_modules from the current folder
// upwards. Node itself only looks upwards from this script's own folder.
function entryFromCurrentFolder() {
  let folder = process.cwd();
  for (;;) {
    const manifest = join(folder, 'node_modules', 'beautiful-mermaid', 'package.json');
    if (existsSync(manifest)) {
      const pkg = JSON.parse(readFileSync(manifest, 'utf8'));
      const declared = pkg.exports?.['.']?.import;
      const entry = typeof declared === 'string' ? declared : (declared?.default ?? pkg.main ?? 'dist/index.js');
      return pathToFileURL(join(dirname(manifest), entry)).href;
    }
    const parent = dirname(folder);
    if (parent === folder) return null;
    folder = parent;
  }
}

async function loadRenderer() {
  try {
    return await import('beautiful-mermaid');
  } catch {
    const entry = entryFromCurrentFolder();
    if (entry !== null) return import(entry);
  }
  return fail(
    3,
    'beautiful-mermaid is not installed, so no picture was made.\n' +
      'Deliver the Mermaid block alone and say the picture was not rendered.\n' +
      'To render, the user can run: npm install beautiful-mermaid',
  );
}

const escapeXml = (text) => text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const args = parseArgs(process.argv.slice(2));
const inputPath = resolve(args.input);
let text;
try {
  text = readFileSync(inputPath, 'utf8');
} catch (error) {
  fail(1, `cannot read ${args.input}: ${error.code ?? error.message}`);
}

const isMarkdown = ['.md', '.markdown'].includes(extname(inputPath).toLowerCase());
let source = text;
if (isMarkdown) {
  const blocks = mermaidBlocks(text);
  if (blocks.length === 0) fail(1, `${args.input} has no mermaid block`);
  if (args.block > blocks.length) fail(1, `${args.input} has ${blocks.length} mermaid block(s), not ${args.block}`);
  source = blocks[args.block - 1];
}

const header = source.match(/^\s*---\s*\n([\s\S]*?)\n---\s*\n/);
const titleLine = header ? header[1].match(/^title:\s*(.+?)\s*$/m) : null;
const title = titleLine ? titleLine[1].replace(/^["']|["']$/g, '') : '';
const body = header ? source.slice(header[0].length) : source;

const renderer = await loadRenderer();

if (args.ascii) {
  try {
    process.stdout.write(renderer.renderMermaidASCII(body) + '\n');
  } catch (error) {
    fail(2, `could not draw the diagram: ${error.message ?? error}`);
  }
  process.exit(0);
}

let svg;
try {
  svg = renderer.renderMermaidSVG(body, HOUSE);
} catch (error) {
  fail(2, `could not draw the diagram: ${error.message ?? error}`);
}

svg = svg.replace(/^\s*@import url\('https:\/\/fonts\.googleapis\.com[^\n]*\n/gm, '');
if (title) svg = svg.replace(/(<svg\b[^>]*>)/, `$1<title>${escapeXml(title)}</title>`);

const stem = basename(inputPath, extname(inputPath));
const outPath = args.out
  ? resolve(args.out)
  : join(dirname(inputPath), isMarkdown ? `${stem}-${args.block}.svg` : `${stem}.svg`);
writeFileSync(outPath, svg);

console.log(`wrote ${outPath} (${Buffer.byteLength(svg)} bytes)`);
console.log(title ? `title, for the caption and the alt text: ${title}` : 'no title in the header: write the caption by hand');
