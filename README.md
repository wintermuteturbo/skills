# Skills

Agent skills I write and use, one folder per skill:

```text
skills/
  <name>/
    SKILL.md
    …                 scripts, references, assets the skill uses
```

Each `SKILL.md` follows the [Agent Skills format](https://agentskills.io/specification): `name` and `description` in its frontmatter, then the instructions.

## Install

With [skilletor](https://skilletor.bartoldi.xyz), for every agent at once, at user scope:

```sh
skilletor add -g wintermuteturbo/skills
```

`skilletor update -g` shows what changed before moving to it.

To version a skill on its own, tag it as `<name>@<version>`, for example `git tag docs@0.1.0`.

## Licence

Each skill carries its own licence in its folder's `LICENSE` file and its `license` frontmatter. `diagrams`, `reader-first-docs` and `skilletor` are MIT OR Apache-2.0, at your option.

`skills/skilletor` is a copy of the skill that ships with skilletor and teaches agents to use it. Its source is skilletor's own repository, so change it there; each copy here is tagged `skilletor@<version>` after the skilletor release it describes.
