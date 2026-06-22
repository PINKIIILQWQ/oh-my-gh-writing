# GitHub Markdown Tools

Use this reference when a GitHub artifact needs badges, alerts, collapsible sections, Mermaid diagrams, tables, images, or other Markdown presentation tools.

## General Rules

- Use presentation tools to clarify content, not decorate it.
- Keep Markdown portable for GitHub rendering.
- Prefer simple Markdown before HTML. Use HTML only when GitHub Markdown cannot express the needed layout, such as centered logo blocks or linked icons.
- Do not wrap a whole artifact in a fenced block.
- Do not add visual elements without a real target, source, or user value.

## Badges

Badges should be useful navigation or status signals. They are not a checklist of every service in the repository.

Recommended badge order:

1. CI / build status when workflow exists.
2. Package or release version when published.
3. License when a license file exists.
4. Downloads or install stats when a real source exists.
5. Security, docs, social, or scenario count only when relevant.

Rules:

- Dynamic badges are only for real data sources such as packages, releases, workflows, coverage, downloads, or stars.
- Static badges can express artifact format or scope, such as `format-SKILL.md` or `18 artifact standards + 7 workflow packs`, but must link to the relevant file or docs.
- Special growth or trend badges, such as Trendshift or Star History, require a verified service URL or repository identifier. Do not invent GitHub Trending status or Trendshift ids.
- Avoid duplicate intent. Do not show both package version and release version unless both matter.
- If a badge URL produces `error`, `unknown`, or a broken image, remove it.
- Link badges to useful destinations: license file, releases page, CI workflow, docs, package registry, or index.

## Alerts

Use GitHub alerts sparingly:

```markdown
> [!NOTE]
> Useful context.

> [!IMPORTANT]
> Critical constraint.

> [!WARNING]
> Risk or destructive action.
```

Use alerts for constraints, risks, migration warnings, or high-value notes. Do not use alerts for ordinary paragraphs.

## Collapsible Sections

Use `<details>` when optional content is long but still useful:

```markdown
<details>
<summary>Full environment details</summary>

Content here.

</details>
```

Rules:

- Keep the summary short.
- Put blank lines after `<summary>` and before `</details>`.
- Do not hide critical migration steps, breaking changes, or reproduction steps inside collapsed content.

## Mermaid

When a GitHub artifact needs a Mermaid diagram, read `mermaid.md` before drafting it. That reference defines diagram selection, evidence boundaries, GitHub-compatible syntax, and output checks.

## Tables

Use tables for comparable data with stable columns, such as support matrices, scenario lists, file indexes, package options, and compatibility matrices.

Rules:

- Keep tables under 5 columns when possible.
- Split long cells into separate bullets or sections.
- Add blank lines before and after tables.
- Do not use tables for prose paragraphs.

## Images and Icons

Use images only when they show the product, output, architecture, screenshot, logo, or actual visual state.

Rules:

- Logos should use repository assets when available.
- Brand/tool icons should link to official docs, site, or repository.
- Use stable icon sources. If an icon is broken, omit it rather than inventing one.
- Tables default to `width="24" height="24"` for icons; compact tables may use 18px.

## Emoji

Use emoji only when the user asks, the repository already uses emoji, or the README style calls for lightweight section markers.

Rules:

- Keep emoji consistent across heading levels.
- Do not use emoji in every bullet.
- For commit or PR title emoji conventions, read `emoji-guide.md`.

## Recommended Tool by Artifact

| Artifact | Useful tools |
|----------|--------------|
| README | Badges, support tables, file index, icons, optional Mermaid |
| Release Notes | Highlights, changelog links, warnings for breaking changes |
| Migration Guide | Warning alerts, before/after tables, compatibility tables |
| PR Description | Checklist, screenshots, local code blocks |
| Issue Form YAML | Valid YAML only; avoid Markdown wrappers in file output |
| RFC | Diagrams, tradeoff tables, details for alternatives |

## Checklist

- [ ] Visual element has a real purpose.
- [ ] Links and image sources are valid or omitted.
- [ ] Tables are readable and not overloaded.
- [ ] Critical information is not hidden in collapsed sections.
- [ ] Markdown renders correctly on GitHub.
