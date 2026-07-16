# BrioHR Knowledge Base (bundled)

**Do not edit these files by hand.** This directory is a read-only snapshot of the
BrioHR product documentation, scraped daily from the
[Help Center](https://support.briohr.com/knowledge).

It is bundled here so the skill can ground its output in real, documented behavior
**offline** — no Cowork Project sync, no GitHub attachment, no connector.

## How it stays current

`.github/workflows/kb-sync.yml` runs daily: it re-scrapes the Help Center with
`scripts/kb/scraper.py`, vendors the result into every skill's `knowledge-base/`,
and — if any article or the catalog changed — cuts a **patch** release, so every
PM's plugin auto-updates. Any hand edit here is overwritten on the next run.

> The scraper is a pristine copy of the one in
> [`BrioHR/knowledge-base`](https://github.com/BrioHR/knowledge-base) (the shared
> single source of truth); both mirror the same Help Center.

## Layout

```
INDEX.md          # master index: categories → subcategories → article links + counts
sitemap.json      # machine-readable: category → subcategory → { title, url }
VERSION           # CalVer of the snapshot, e.g. 2026.07.16
<category>/<subcategory>/*.md   # the articles (YAML frontmatter + Markdown body)
```

## How the skill should read it

1. Open `INDEX.md` (or `sitemap.json`) and find the category/subcategory for the topic.
2. Open the specific article `.md` under `<category>/<subcategory>/`.
3. Each article starts with frontmatter (`title`, `category`, `subcategory`,
   `source_url`, `date`) followed by the Markdown body.

Prefer reading the one relevant article over loading `INDEX.md` wholesale.
