# Final Output Format

Use this exact structure when presenting the generated test cases. Only include sections the PM marked **Yes** or **Add** during sequential confirmation. Skip sections marked **No** completely — no heading, no placeholder.

## Format

```markdown
# Test Cases — [Ticket Key] [Ticket Title]

**Ticket:** [B2-1234](https://briohr.atlassian.net/browse/B2-1234)
**Module:** [ModuleName]
**Platform:** [Web / Mobile / Superadmin / Web + Mobile]

---

**Initialization & Migration**
1. Test scenario one.
2. Test scenario two.
3. Test scenario three.

**Regression**
1. Test scenario one.
2. Test scenario two.

**Happy Flow / Smoke Test**
1. Test scenario one.
2. Test scenario two.
3. Test scenario three.

**Integration / Interaction**
1. Test scenario one.
2. Test scenario two.

**Platform Coverage**
1. Test scenario one. (Web)
2. Test scenario two. (Mobile — Android)
3. Test scenario three. (Mobile — iOS)
4. Test scenario four. (Mobile — Huawei)
5. Test scenario five. (Superadmin)

**Edge Cases**
1. Test scenario one.
2. Test scenario two.
3. Test scenario three.
```

If there are open questions surfaced during context gathering (genuinely ambiguous points the ticket does not resolve), append a final block:

```markdown
---

**Open Questions**
- Question one — needs clarification before testing.
- Question two — needs clarification before testing.
```

## Rules

- Section headings are bold prose (e.g., `**Regression**`), not Markdown `##` headings — keeps the output compact for pasting into Jira comments.
- Numbered list per section, restarting at 1.
- One scenario per line. No sub-bullets, no nested lists.
- Each scenario is one sentence in imperative form.
- For Platform Coverage scenarios, append a short platform tag in parentheses at the end of the line — e.g., `(Web)`, `(Mobile — Android)`, `(Mobile — iOS)`, `(Mobile — Huawei)`, `(Superadmin)` — so the developer knows exactly which platform to test on.
- Do not include sections the PM said No to. Do not write "(skipped)" or "N/A" — just omit the heading entirely.
- The header lines (Ticket, Module, Platform) help the developer trace context. Keep them.
- For payroll scenarios, include the salary amount used in the test data (e.g., "Run payroll for an employee with MYR 5,000 basic salary and verify EPF deduction is correct").
