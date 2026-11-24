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

skilletor reads this private repository with your own git access (SSH keys or a credential helper) and stores no credentials. `skilletor update -g` shows what changed before moving to it.

To version a skill on its own, tag it as `<name>@<version>`, for example `git tag docs@0.1.0`.

## Licence

Not open source yet: all rights reserved until a licence is added.
