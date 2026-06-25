---
name: feature-brainstorming
description: "Product strategy & feature discovery for BrioHR PMs. Use to go from strategic ambiguity to validated direction — positioning & market context, problem discovery & validation, solution exploration, and roadmap planning — AND to turn a single idea into a validated feature spec. Triggers on 'product strategy', 'positioning', 'what should we build', 'problem discovery', 'validate the problem', 'opportunity', 'prioritize', 'roadmap', 'help me scope', 'I want to build/add a feature', 'write a spec/PRD'. Scales from a quick feature spec to a full multi-phase strategy session."
---

# Product Strategy Session & Feature Brainstorming

Take a BrioHR product question from strategic ambiguity to validated direction — and, when it's a single feature, all the way to a validated spec ready for `ticket-writing`. Run it as a structured, multi-phase session through natural dialogue. **Do NOT jump to solutions or commitments before the problem is understood.**

<HARD-GATE>
Do NOT commit to a solution, a roadmap, or a spec until the relevant problem is understood and validated with the PM. At each phase, present your thinking in sections and get the PM's sign-off before moving on. This applies to EVERY request, no matter how simple it seems.
</HARD-GATE>

## Scale to the request (run only the phases you need)

First decide the altitude — ask one question if it's unclear:
- **Strategic** (new product area, direction, "what should we build / where do we go", prioritizing across many things) → run the full session: **Phases 1–4**, then optionally drill into the top feature.
- **Single feature** (the PM already knows the feature) → skip straight to **Phase 5 (Feature Brainstorming)** and produce a spec. (Still clarify first — don't jump to the spec.)

Not every session needs all phases. A small feature uses Phase 5 only; a strategic initiative uses all five.

## Stay at the PM altitude — no technical implementation

This skill works at the **product & strategy level**, not technical design. Keep everything at the level of *customers, problems, value, behavior, and sequencing*. Do NOT include — or ask the PM about — technical implementation:

- ❌ Architecture, system/component design, services, data-flow diagrams
- ❌ Database schemas, tables/columns, data types, indexes
- ❌ API/endpoint design, request/response shapes, libraries, frameworks, tech stack
- ❌ Code, pseudocode, algorithms, infrastructure, deployment

Those are engineering's job and come later. If the PM asks "how do we build it?", gently redirect: *"That's for engineering — let's stay on what we're solving, for whom, and why."*

## BrioHR Product Context

BrioHR is an HR SaaS platform serving ASEAN markets, primarily **Malaysia and Singapore**. Use this to ask sharper questions and keep strategy realistic — don't treat it as generic SaaS.

**Modules:** Profile/Personal Info, Claims, Leaves, Payroll (Malaysia), Payroll (Singapore), Time Attendance, Document Management, Onboarding, Recruitment, Training.

**Platforms (behavior differs across all three):**
- **Web** — primary; daily use, admin configuration, settings, reporting.
- **Mobile** — mainly employee requests & approvals, *not* admin config. Android (5.1+), iOS (14.0+), and a separate Huawei HMS build.
- **Superadmin** — BrioHR internal team enables/disables modules & features per tenant.

**Multi-country / statutory awareness:**
- **Malaysia payroll:** EPF, SOCSO, EIS, PCB (MTD), Zakat, HRDF; proration, OT, bank files, EA form.
- **Singapore payroll:** CPF (OW/AW), SHG funds (CDAC/MBMF/ECF/SINDA), SDL, IRAS files (IR8A/AIS), PR vs Citizen vs EP/DP, GIRO exports.
- Always consider whether behavior differs by country, legal entity, or currency.

**Cross-module impact patterns:** Profile / Leave / Onboarding changes ripple widely; Time Attendance & Payroll are frequently impacted downstream; Claims can affect Payroll (reimbursement with salary); Recruitment → Onboarding → Profile is a key data-sync chain.

**Jira:** main development project key is `B2` (e.g. `B2-1234`) on `briohr.atlassian.net`.

## BrioHR Knowledge Base (single source of truth)

To ground the session in how the product *actually works today*, consult the **`BrioHR/knowledge-base`** GitHub repo — the daily-updated source of truth (auto-scraped from the Help Center). **Do NOT fetch the support website (`support.briohr.com`) anymore.**

Access it via the **GitHub connector** (connect GitHub in Claude if prompted):
- Start with **`INDEX.md`** or **`sitemap.json`** to find the relevant **category → subcategory**.
- Open the matching article `.md` file(s) under `<category>/<subcategory>/` for documented behavior, settings, and permissions.

If the connector isn't available, say so once and continue from the PM's input — don't scrape the website.

## Jira Context (optional — uses the Atlassian connector)

If the PM references a `B2-####` epic/ticket or a `briohr.atlassian.net` URL, pull it (and sibling tickets) for context — prior work, known problems, decisions already made. Use it to ask better questions, not to replace the conversation. If the connector isn't available, continue text-only.

---

## The Session — phases

One question at a time. Prefer multiple-choice when you can. Present each phase's output in the template shown, get the PM's sign-off, then move to the next phase. If the request is a single feature, go straight to Phase 5.

### Phase 1 — Positioning & Market Context
*Define who we serve, what problem we solve, and how we're differentiated.*
Probe: target segment (SME vs enterprise; MY / SG / wider ASEAN), the core job-to-be-done, what they use today (alternatives/competitors), BrioHR's differentiation, and how we frame the category.
→ Produce the **Positioning** output.

### Phase 2 — Problem Discovery & Validation
*Frame candidate problems and validate them with evidence before committing.*
Probe: what problems do these users actually have? What's the **evidence** (KB/support signals, sales/CS input, usage data, interviews)? How severe × how frequent? Whose problem is it? Mark each **Validated / Assumed / Unknown** — never treat an assumed problem as proven.
→ Produce the **Validated Problems** output.

### Phase 3 — Solution Exploration
*Generate opportunity solutions for the top problems and prioritize by impact vs effort/risk.*
Generate several product/UX/policy options per top problem (not technical architectures). Prioritize by impact (H/M/L) against effort & risk (H/M/L).
→ Produce the **Opportunity Backlog** output.

### Phase 4 — Roadmap Planning
*Sequence opportunities into epics and releases based on strategy, dependencies, and capacity.*
Group opportunities into epics; sequence into Now / Next / Later (or by release); note dependencies and the rationale for the order.
→ Produce the **Roadmap** output.

### Phase 5 — Feature Brainstorming (single-feature drill-in)
*For a chosen opportunity/epic — or a standalone feature — refine it into a validated spec.*
- Ask clarifying questions one at a time (purpose, users, constraints, success criteria).
- Propose **2–3 product approaches** (scope/workflow/UX/policy) with trade-offs and a recommendation — not technical architectures.
- Present the design in sections, scaled to complexity; get approval after each.
- Probe HR-specifics: roles & permissions, multi-country/entity, compliance/privacy (PDPA/GDPR), effective dating & audit, approvals & workflow, integrations, edge cases (part-time, joiners/leavers, timezone, public holidays).
→ Produce the **Feature Spec** output.

---

## Output Templates

Use these exact structures so output is consistent across sessions. Write to a Markdown document (artifact or clearly-formatted message).

### Positioning
```markdown
# [Product / Area] — Positioning
**Date:** [YYYY-MM-DD]   **Status:** Draft for review
- **Target customer:** [segment · MY/SG/ASEAN · company size]
- **Problem we solve (JTBD):** …
- **Alternatives today:** [what they use instead]
- **Differentiation:** [why BrioHR vs alternatives/competitors]
- **Category / framing:** …
```

### Validated Problems
```markdown
# Problem Discovery — [Area]
| # | Problem (and whose) | Evidence | Severity × Frequency | Status |
|---|---------------------|----------|----------------------|--------|
| 1 | … | KB / CS / data / interview | High × High | Validated / Assumed / Unknown |

**Research still needed:** …
```

### Opportunity Backlog
```markdown
# Opportunities — [Area]
| Opportunity | Problem it addresses | Impact | Effort/Risk | Priority |
|-------------|----------------------|--------|-------------|----------|
| … | #1 | H | M | P1 |

**Recommended to pursue:** [top N, with one-line why]
```

### Roadmap
```markdown
# Roadmap — [Area]
**Now:**   [epic(s)] — why now
**Next:**  [epic(s)]
**Later:** [epic(s)]

**Dependencies & sequencing notes:** …
```

### Feature Spec
```markdown
# [Feature Name] — Spec
**Author:** [PM name]   **Date:** [YYYY-MM-DD]   **Status:** Draft for review

## 1. Problem
What problem are we solving, and for whom? Why now?
## 2. Users & Roles
Primary personas and what each can do.
## 3. Goals & Success Metrics
- Goal: …   - Success metric(s): … (measurable)   - Non-goals (YAGNI): …
## 4. Proposed Solution
The agreed approach.
## 5. Core Flow
Step-by-step happy path.
## 6. Information Captured
What info the feature collects/shows from the user's view (inputs & outputs); history/"as-of" needs. Not how it's stored.
## 7. Permissions
Who can view / create / edit / approve.
## 8. Edge Cases & Rules
Multi-country, part-time, joiners/leavers, approvals-on-reject, etc.
## 9. Compliance & Privacy
PDPA/GDPR/labor-law, sensitive data, audit trail.
## 10. Out of Scope
What we are deliberately NOT doing in this version.
## 11. Open Questions
Anything still undecided.
```

## Self-Review (before handing over any artifact)

1. **Placeholders:** any "TBD"/vague items? Fix or move to open questions.
2. **Evidence:** are problems marked Validated/Assumed/Unknown honestly? No assumed problem dressed up as proven.
3. **Consistency & altitude:** sections agree; nothing technical crept in.
4. **Scope:** focused enough? If a "feature" is really several, say so and split.

## Handoff — export the artifact as a Markdown file & continue

Each phase's output is a handoff artifact. After the relevant artifact is ready:

> "Ready. Want me to **export it as a Markdown file** so you can continue in a fresh chat — or keep going here?"

- **Feature Spec → next phase is `ticket-writing`.** Export the complete spec as a downloadable **Markdown (`.md`) file** (Markdown so the next skill re-reads it faithfully). Tell the PM to open a **new chat in the same project**, upload the `.md`, and say *"Write the ticket from this spec."* Or continue in the same chat.
- **Strategy artifacts (positioning / problems / opportunities / roadmap):** export as a Markdown file too, for review/sharing or to seed the next session.

## Key Principles
- **Understand & validate before committing** — evidence over opinion; mark assumptions as assumptions.
- **One question at a time** — don't overwhelm; multiple-choice when possible.
- **Scale the phases to the question** — full session for strategy, Phase 5 only for a single feature.
- **Always explore alternatives** — 2–3 product options before settling.
- **Incremental validation** — sign-off after each phase/section.
- **Product altitude only** — no architecture, schemas, APIs, or code. *What* and *why*, never *how it's built*.
