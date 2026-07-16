# BrioHR Knowledge Base (vendored)

**Do not edit these files by hand.** This directory is a read-only snapshot of the
[`BrioHR/knowledge-base`](https://github.com/BrioHR/knowledge-base) repo — the single
source of truth for BrioHR product documentation, scraped daily from the
[Help Center](https://support.briohr.com/knowledge).

It is vendored here so the skills can ground their output in real, documented
behavior **offline** — no Cowork Project sync, no GitHub attachment, no connector.

## How it stays current

`.github/workflows/kb-sync.yml` runs daily: it pulls the latest built Markdown from
`BrioHR/knowledge-base` and, if anything changed, pushes the update to `main`. That
push triggers a **patch** release, so every PM's plugin auto-updates. Any hand edit
here is overwritten on the next sync.

## Layout

```
INDEX.md          # master index: categories → subcategories → article links + counts
sitemap.json      # machine-readable: category → subcategory → { title, url }
VERSION           # CalVer of the source snapshot, e.g. 2026.07.15
<category>/<subcategory>/*.md   # the articles (YAML frontmatter + Markdown body)
```

## How skills should read it

1. Open `INDEX.md` (or `sitemap.json`) and find the category/subcategory for the topic.
2. Open the specific article `.md` under `<category>/<subcategory>/`.
3. Each article starts with frontmatter (`title`, `category`, `subcategory`,
   `source_url`, `date`) followed by the Markdown body.

Prefer reading the one relevant article over loading `INDEX.md` wholesale.
