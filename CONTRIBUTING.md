# Contributing

To add or update an entry, open a PR editing the relevant file in `docs/`.

## Entry format

### Tools hosted on GitHub

```markdown
### [Tool Name](https://github.com/owner/repo)
**Release:** [check pending](https://github.com/owner/repo/releases/latest)
Short description. What it does and when you'd use it (1-2 sentences).
```

Use exactly `[check pending](https://github.com/owner/repo/releases/latest)` as the placeholder. The weekly action will replace it with the actual latest version on the next run.

### Tools not on GitHub (forums, websites, etc.)

```markdown
### [Tool Name](https://link-to-tool.com)
Short description.
```

Omit the `**Release:**` line entirely — the action only tracks GitHub repos.

## Which file to edit

| Category | File |
|---|---|
| Lua scripting frameworks | `docs/scripting-frameworks.md` |
| Standalone mission scripts | `docs/mission-scripts.md` |
| Mission and campaign generators | `docs/mission-generators.md` |
| Server management and comms | `docs/server-tools.md` |
| Dev tools and editors | `docs/dev-tools.md` |
| Free aircraft mods | `docs/aircraft-mods.md` |

## Criteria

- **Useful** to mission designers, server operators, or DCS developers
- **Free** or has a meaningful free tier — paid-only tools go in the "No Release Tracking" section at most
- **Working** — links shouldn't 404, and the tool should be compatible with a current DCS version if applicable
- Clearly **archived or unmaintained** tools are fine to include if still useful, but note it in the description

## PR checklist

- [ ] Added to the correct file
- [ ] GitHub-tracked entry uses the `[check pending](...)` placeholder exactly
- [ ] Description is 1-2 sentences, no marketing language
- [ ] Link goes to the primary source (repo, official site, or original forum thread)
