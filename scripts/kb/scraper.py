#!/usr/bin/env python3
"""
BrioHR Knowledge Base Scraper

Pipeline: discover -> scrape -> clean -> index

Usage:
  python scraper.py              # full refresh (all steps)
  python scraper.py discover     # rebuild sitemap.json from live site
  python scraper.py scrape       # scrape all articles (fresh)
  python scraper.py scrape --resume  # scrape remaining articles
  python scraper.py clean        # remove stale .md files
  python scraper.py index        # regenerate INDEX.md
"""

import argparse
import json
import os
import re
import shutil
import asyncio
from datetime import date
from pathlib import Path
from playwright.async_api import async_playwright

BASE_URL = 'https://support.briohr.com/knowledge'
# Repo root is one level up: this script lives in scripts/, while the knowledge
# base (article directories, INDEX.md, sitemap.json) lives at the repo root.
BASE_DIR = Path(__file__).resolve().parent.parent
SITEMAP_PATH = BASE_DIR / 'sitemap.json'
PROGRESS_PATH = BASE_DIR / 'scrape_progress.json'

# The JavaScript extraction function (tested and verified)
EXTRACT_JS = '''() => {
    function htmlToMarkdown(element) {
        let md = '';

        function processNode(node, listDepth) {
            listDepth = listDepth || 0;
            if (node.nodeType === Node.TEXT_NODE) {
                return node.textContent;
            }
            if (node.nodeType !== Node.ELEMENT_NODE) return '';

            const tag = node.tagName.toLowerCase();
            if (['nav', 'footer', 'script', 'style', 'header', 'noscript'].includes(tag)) return '';

            switch(tag) {
                case 'h1': return '\\n# ' + node.textContent.trim() + '\\n\\n';
                case 'h2': return '\\n## ' + node.textContent.trim() + '\\n\\n';
                case 'h3': return '\\n### ' + node.textContent.trim() + '\\n\\n';
                case 'h4': return '\\n#### ' + node.textContent.trim() + '\\n\\n';
                case 'h5': return '\\n##### ' + node.textContent.trim() + '\\n\\n';
                case 'p': return '\\n' + processChildren(node, listDepth) + '\\n\\n';
                case 'br': return '\\n';
                case 'strong': case 'b': return '**' + processChildren(node, listDepth) + '**';
                case 'em': case 'i': return '*' + processChildren(node, listDepth) + '*';
                case 'a': {
                    const href = node.getAttribute('href') || '';
                    const text = node.textContent.trim();
                    return href ? '[' + text + '](' + href + ')' : text;
                }
                case 'img': {
                    const src = node.getAttribute('src') || '';
                    const alt = node.getAttribute('alt') || 'image';
                    return src ? '\\n![' + alt + '](' + src + ')\\n' : '';
                }
                case 'ul': return '\\n' + processListItems(node, listDepth, false) + '\\n';
                case 'ol': return '\\n' + processListItems(node, listDepth, true) + '\\n';
                case 'li': return processChildren(node, listDepth);
                case 'blockquote': {
                    const c = processChildren(node, listDepth);
                    return '\\n' + c.split('\\n').map(l => '> ' + l).join('\\n') + '\\n\\n';
                }
                case 'code': {
                    if (node.parentElement && node.parentElement.tagName.toLowerCase() === 'pre') {
                        return processChildren(node, listDepth);
                    }
                    return '`' + node.textContent.trim() + '`';
                }
                case 'pre': return '\\n```\\n' + node.textContent.trim() + '\\n```\\n\\n';
                case 'table': return '\\n' + processTable(node) + '\\n\\n';
                case 'hr': return '\\n---\\n\\n';
                case 'iframe': {
                    const src = node.getAttribute('src') || '';
                    return src ? '\\n[Embedded content](' + src + ')\\n\\n' : '';
                }
                default: return processChildren(node, listDepth);
            }
        }

        function processChildren(node, listDepth) {
            let result = '';
            for (const child of node.childNodes) {
                result += processNode(child, listDepth);
            }
            return result;
        }

        function processListItems(listNode, depth, ordered) {
            let result = '';
            let index = 1;
            for (const child of listNode.children) {
                if (child.tagName.toLowerCase() === 'li') {
                    const indent = '  '.repeat(depth);
                    const bullet = ordered ? index + '. ' : '- ';
                    const content = processChildren(child, depth + 1).trim();
                    result += indent + bullet + content + '\\n';
                    index++;
                }
            }
            return result;
        }

        function processTable(tableNode) {
            const rows = tableNode.querySelectorAll('tr');
            if (rows.length === 0) return '';
            let result = '';
            let isFirst = true;
            for (const row of rows) {
                const cells = row.querySelectorAll('th, td');
                const cellTexts = Array.from(cells).map(c => c.textContent.trim().replace(/\\|/g, '\\\\|'));
                result += '| ' + cellTexts.join(' | ') + ' |\\n';
                if (isFirst) {
                    result += '| ' + cellTexts.map(() => '---').join(' | ') + ' |\\n';
                    isFirst = false;
                }
            }
            return result;
        }

        for (const child of element.childNodes) {
            md += processNode(child);
        }
        return md;
    }

    // Title (from HubSpot KB article module)
    const titleEl = document.querySelector('#hs_cos_wrapper_kb-article-module-3_') ||
                    document.querySelector('article h1') ||
                    document.querySelector('h1');
    const title = titleEl ? titleEl.textContent.trim() : document.title;

    // Subtitle
    const subtitleEl = document.querySelector('#hs_cos_wrapper_kb-article-module-4_') ||
                       document.querySelector('article h2');
    const subtitle = subtitleEl ? subtitleEl.textContent.trim() : '';

    // Date
    const timeEl = document.querySelector('article time');
    const date = timeEl ? timeEl.textContent.trim() : '';

    // Body content - the richtext field (HubSpot KB specific selector)
    const bodyEl = document.querySelector('[data-hs-cos-type="inline_richtext_field"]') ||
                   document.querySelector('#hs_cos_wrapper_kb-article-module-5_') ||
                   document.querySelector('.knowledge-article__body') ||
                   document.querySelector('article');
    const body = bodyEl ? htmlToMarkdown(bodyEl) : '';

    return { title, subtitle, date, body, url: window.location.href };
}'''


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[&]', 'and', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text


def load_progress():
    if PROGRESS_PATH.exists():
        with open(PROGRESS_PATH) as f:
            return json.load(f)
    return {'completed': [], 'failed': []}


def save_progress(progress):
    with open(PROGRESS_PATH, 'w') as f:
        json.dump(progress, f, indent=2)


def clean_markdown(text):
    """Clean up extracted markdown."""
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    lines = [line.rstrip() for line in text.split('\n')]
    text = '\n'.join(lines)
    text = text.lstrip('\n')
    return text


def build_article_list(sitemap):
    """Build flat list of articles with their file paths from sitemap."""
    articles = []
    for cat in sitemap:
        for sub in cat.get('subcategories', []):
            sub_slug = slugify(sub['subcategory'])
            for article in sub['articles']:
                dir_path = BASE_DIR / cat['slug'] / sub_slug
                filename = slugify(article['title'])[:80] + '.md'
                file_path = dir_path / filename
                articles.append({
                    'category': cat['category'],
                    'subcategory': sub['subcategory'],
                    'title': article['title'],
                    'url': article['url'],
                    'file_path': str(file_path),
                    'cat_slug': cat['slug'],
                    'sub_slug': sub_slug,
                })
    return articles


# ---------------------------------------------------------------------------
# Step 1: Discover sitemap from live site
# ---------------------------------------------------------------------------

async def discover_sitemap(page):
    """Crawl the live KB site and produce a fresh sitemap."""
    print("=== DISCOVER: Crawling live KB site ===", flush=True)

    await page.goto(BASE_URL, wait_until='domcontentloaded', timeout=30000)
    await page.wait_for_selector('a[href*="/knowledge/"]', timeout=10000)

    # Extract category links from the main KB page
    cat_links = await page.evaluate('''() => {
        const links = Array.from(document.querySelectorAll('a[href*="/knowledge/"]'));
        const results = [];
        const seen = new Set();
        for (const a of links) {
            const href = a.getAttribute('href') || '';
            // Match /knowledge/<slug> (exactly 2 segments, allow query params)
            const match = href.match(/\\/knowledge\\/([a-z0-9-]+)\\/?(?:\\?.*)?$/);
            if (!match) continue;
            const slug = match[1];
            // Skip anchor links, the base /knowledge page itself, and article-like deep links
            if (href.includes('#') || seen.has(slug)) continue;
            seen.add(slug);
            results.push({ name: a.textContent.trim(), slug, url: a.href });
        }
        return results;
    }''')

    print(f"Found {len(cat_links)} categories", flush=True)
    sitemap = []

    for ci, cat in enumerate(cat_links):
        print(f"  [{ci+1}/{len(cat_links)}] {cat['name']} ({cat['slug']})", flush=True)

        await page.goto(cat['url'], wait_until='domcontentloaded', timeout=30000)
        await page.wait_for_timeout(500)

        # Click all toggle buttons to expand hidden articles
        toggles = await page.query_selector_all('.hs-kb-category-article-list__toggle')
        for toggle in toggles:
            try:
                await toggle.click()
            except Exception:
                pass
        if toggles:
            await page.wait_for_timeout(500)

        # Extract subcategories and their articles
        subcategories = await page.evaluate('''() => {
            const subs = [];
            // Each subcategory is wrapped in .hs-kb-subcategory-listing with h2 + ul
            const sections = document.querySelectorAll('.hs-kb-subcategory-listing');

            if (sections.length > 0) {
                // Structured subcategories
                for (const section of sections) {
                    const h2 = section.querySelector('h2');
                    const heading = h2 ? h2.textContent.trim() : 'General';
                    const items = section.querySelectorAll('ul.hs-kb-category-article-list li a');
                    const articles = [];
                    for (const a of items) {
                        const href = a.getAttribute('href') || '';
                        if (!href || href.startsWith('#') || href === '/') continue;
                        if (!href.includes('/knowledge/')) continue;
                        articles.push({ title: a.textContent.trim(), url: a.href });
                    }
                    if (articles.length > 0) {
                        subs.push({ subcategory: heading, articles });
                    }
                }
            } else {
                // Flat list fallback (no subcategory wrappers)
                const items = document.querySelectorAll('ul.hs-kb-category-article-list li a');
                const articles = [];
                for (const a of items) {
                    const href = a.getAttribute('href') || '';
                    if (!href || href.startsWith('#') || href === '/') continue;
                    if (!href.includes('/knowledge/')) continue;
                    articles.push({ title: a.textContent.trim(), url: a.href });
                }
                if (articles.length > 0) {
                    subs.push({ subcategory: 'General', articles });
                }
            }
            return subs;
        }''')

        total = sum(len(s['articles']) for s in subcategories)
        print(f"    {len(subcategories)} subcategories, {total} articles", flush=True)

        sitemap.append({
            'category': cat['name'],
            'slug': cat['slug'],
            'subcategories': subcategories,
        })

        await page.wait_for_timeout(300)

    # Save sitemap
    with open(SITEMAP_PATH, 'w') as f:
        json.dump(sitemap, f, indent=2)

    total_articles = sum(
        len(a) for cat in sitemap for sub in cat['subcategories'] for a in [sub['articles']]
    )
    print(f"\nSitemap saved: {len(sitemap)} categories, {total_articles} articles", flush=True)
    return sitemap


# ---------------------------------------------------------------------------
# Step 2: Scrape articles
# ---------------------------------------------------------------------------

async def do_scrape(page, sitemap, resume=False):
    """Scrape all articles from sitemap. If resume=True, skip already-completed URLs."""
    print("=== SCRAPE: Downloading articles ===", flush=True)

    if resume:
        progress = load_progress()
    else:
        progress = {'completed': [], 'failed': []}
        save_progress(progress)

    completed_urls = set(progress['completed'])
    articles = build_article_list(sitemap)
    remaining = [a for a in articles if a['url'] not in completed_urls]

    print(f"Total articles: {len(articles)}", flush=True)
    print(f"Already completed: {len(completed_urls)}", flush=True)
    print(f"Remaining: {len(remaining)}", flush=True)

    if not remaining:
        print("All articles already scraped!", flush=True)
        return

    for i, article in enumerate(remaining):
        try:
            print(f"[{i+1}/{len(remaining)}] {article['category']} > {article['subcategory']} > {article['title'][:60]}...", flush=True)

            # Use domcontentloaded instead of networkidle to avoid Loom embed timeouts
            await page.goto(article['url'], wait_until='domcontentloaded', timeout=30000)
            await page.wait_for_selector(
                '[data-hs-cos-type="inline_richtext_field"], article',
                timeout=10000,
            )

            content = await page.evaluate(EXTRACT_JS)

            # Build markdown file
            title = content.get('title', article['title'])
            subtitle = content.get('subtitle', '')
            article_date = content.get('date', '')
            body = clean_markdown(content.get('body', ''))

            # Remove the h1 title from body if duplicated
            if body.startswith(f"# {title}"):
                body = body[len(f"# {title}"):].lstrip('\n')

            md = f"---\n"
            md += f"title: \"{title}\"\n"
            md += f"category: \"{article['category']}\"\n"
            md += f"subcategory: \"{article['subcategory']}\"\n"
            md += f"source_url: \"{article['url']}\"\n"
            if article_date:
                md += f"date: \"{article_date}\"\n"
            md += f"---\n\n"
            md += f"# {title}\n\n"
            if subtitle:
                md += f"*{subtitle}*\n\n"
            md += body

            os.makedirs(os.path.dirname(article['file_path']), exist_ok=True)
            with open(article['file_path'], 'w', encoding='utf-8') as f:
                f.write(md)

            progress['completed'].append(article['url'])

            if (i + 1) % 10 == 0:
                save_progress(progress)
                print(f"  Progress saved ({len(progress['completed'])} completed)", flush=True)

            await page.wait_for_timeout(300)

        except Exception as e:
            print(f"  ERROR: {e}", flush=True)
            progress['failed'].append({'url': article['url'], 'error': str(e)})
            if (i + 1) % 10 == 0:
                save_progress(progress)

    save_progress(progress)
    print(f"\nScrape done! Completed: {len(progress['completed'])}, Failed: {len(progress['failed'])}", flush=True)


# ---------------------------------------------------------------------------
# Step 3: Clean stale files
# ---------------------------------------------------------------------------

def clean_stale_files(sitemap):
    """Remove .md files that are not in the current sitemap."""
    print("=== CLEAN: Removing stale files ===", flush=True)

    # Build set of expected file paths from sitemap
    expected = set()
    for cat in sitemap:
        for sub in cat.get('subcategories', []):
            sub_slug = slugify(sub['subcategory'])
            for article in sub['articles']:
                filename = slugify(article['title'])[:80] + '.md'
                expected.add(str(BASE_DIR / cat['slug'] / sub_slug / filename))

    # Find all .md files under category directories (skip INDEX.md and top-level files)
    removed = 0
    cat_slugs = {cat['slug'] for cat in sitemap}
    for cat_dir in BASE_DIR.iterdir():
        if not cat_dir.is_dir() or cat_dir.name.startswith('.'):
            continue
        for md_file in cat_dir.rglob('*.md'):
            if str(md_file) not in expected:
                print(f"  Removing stale: {md_file.relative_to(BASE_DIR)}", flush=True)
                md_file.unlink()
                removed += 1

    # Remove empty directories
    removed_dirs = 0
    for cat_dir in BASE_DIR.iterdir():
        if not cat_dir.is_dir() or cat_dir.name.startswith('.'):
            continue
        for sub_dir in list(cat_dir.iterdir()):
            if sub_dir.is_dir() and not any(sub_dir.iterdir()):
                print(f"  Removing empty dir: {sub_dir.relative_to(BASE_DIR)}", flush=True)
                sub_dir.rmdir()
                removed_dirs += 1
        # Check if category dir itself is now empty
        if not any(cat_dir.iterdir()):
            # Only remove if not a known category
            if cat_dir.name not in cat_slugs:
                print(f"  Removing empty dir: {cat_dir.relative_to(BASE_DIR)}", flush=True)
                cat_dir.rmdir()
                removed_dirs += 1

    print(f"Cleaned {removed} stale files, {removed_dirs} empty directories", flush=True)


# ---------------------------------------------------------------------------
# Step 4: Generate INDEX.md
# ---------------------------------------------------------------------------

def generate_index(sitemap):
    """Regenerate INDEX.md from the sitemap."""
    print("=== INDEX: Regenerating INDEX.md ===", flush=True)

    today = date.today().isoformat()
    lines = []
    lines.append("# BrioHR Knowledge Base - Documentation Index\n")
    lines.append(f"> Auto-extracted from [BrioHR Help Center]({BASE_URL})")
    lines.append(f"> Last updated: {today}\n")
    lines.append("---\n")

    # Table of Contents
    lines.append("## Table of Contents\n")
    for cat in sitemap:
        cat_anchor = slugify(cat['category'])
        total = sum(len(sub['articles']) for sub in cat.get('subcategories', []))
        lines.append(f"- [{cat['category']}](#{cat_anchor}) ({total} articles)")
        for sub in cat.get('subcategories', []):
            sub_anchor = f"{cat_anchor}-{slugify(sub['subcategory'])}"
            lines.append(f"  - [{sub['subcategory']}](#{sub_anchor}) ({len(sub['articles'])})")
    lines.append("")

    # Per-category sections
    for cat in sitemap:
        cat_anchor = slugify(cat['category'])
        total = sum(len(sub['articles']) for sub in cat.get('subcategories', []))
        lines.append("---\n")
        lines.append(f"## {cat['category']}\n")
        lines.append(f"**{total} articles** | [Browse category]({cat['slug']}/)\n")

        for sub in cat.get('subcategories', []):
            sub_slug = slugify(sub['subcategory'])
            lines.append(f"### {cat['category']} - {sub['subcategory']}\n")
            lines.append(f"**{len(sub['articles'])} articles** | Directory: `{cat['slug']}/{sub_slug}/`\n")

            for article in sub['articles']:
                filename = slugify(article['title'])[:80] + '.md'
                rel_path = f"{cat['slug']}/{sub_slug}/{filename}"
                lines.append(f"- [{article['title']}]({rel_path})")
            lines.append("")

    lines.append("---\n")

    index_path = BASE_DIR / 'INDEX.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"INDEX.md regenerated ({len(sitemap)} categories)", flush=True)


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

async def run(args):
    command = args.command

    if command in ('refresh', 'discover', 'scrape'):
        # These commands need a browser
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 900},
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            )
            page = await context.new_page()

            try:
                if command == 'refresh':
                    sitemap = await discover_sitemap(page)
                    await do_scrape(page, sitemap, resume=False)
                    clean_stale_files(sitemap)
                    generate_index(sitemap)
                elif command == 'discover':
                    await discover_sitemap(page)
                elif command == 'scrape':
                    with open(SITEMAP_PATH) as f:
                        sitemap = json.load(f)
                    await do_scrape(page, sitemap, resume=args.resume)
            finally:
                await browser.close()

    elif command == 'clean':
        with open(SITEMAP_PATH) as f:
            sitemap = json.load(f)
        clean_stale_files(sitemap)

    elif command == 'index':
        with open(SITEMAP_PATH) as f:
            sitemap = json.load(f)
        generate_index(sitemap)


def parse_args():
    parser = argparse.ArgumentParser(description='BrioHR Knowledge Base Scraper')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('refresh', help='Full pipeline: discover + scrape + clean + index')
    subparsers.add_parser('discover', help='Crawl live site and rebuild sitemap.json')

    scrape_parser = subparsers.add_parser('scrape', help='Scrape articles from sitemap.json')
    scrape_parser.add_argument('--resume', action='store_true', help='Resume from last progress')

    subparsers.add_parser('clean', help='Remove stale .md files not in sitemap')
    subparsers.add_parser('index', help='Regenerate INDEX.md from sitemap')

    args = parser.parse_args()
    if args.command is None:
        args.command = 'refresh'
    return args


if __name__ == '__main__':
    args = parse_args()
    asyncio.run(run(args))
