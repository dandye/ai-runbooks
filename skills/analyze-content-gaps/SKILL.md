---
name: analyze-content-gaps
description: >
  Identify missing, thin, redundant, and outdated content within a documentation set.
  Compares existing coverage against user needs and competitive benchmarks, then produces
  a prioritized gap analysis report with consolidation targets.
  Use when the user asks to find missing content, identify duplicate pages, audit
  documentation coverage, consolidate wiki pages, or analyze what topics are underdocumented.
---

# Analyze Content Gaps

## Process

### 1. Baseline assessment

Map current content at the target path:

```bash
# count files by type
find <PATH> -name "*.md" -o -name "*.mdx" -o -name "*.rst" | wc -l

# extract all H1/H2 headings for topic inventory
grep -rh "^##\? " <PATH> --include="*.md" | sort | uniq -c | sort -rn
```

**Verify:** confirm file list is non-empty before proceeding. If zero files found, ask the user for the correct path.

### 2. Needs analysis

Determine what *should* be covered by checking available signals:

| Signal | How to check | What it reveals |
|---|---|---|
| Search logs | grep analytics/search-queries if available | Topics users look for but can't find |
| Support tickets | scan recent issues for recurring questions | Knowledge gaps causing friction |
| Competitor docs | compare table of contents against similar projects | Industry-standard topics you're missing |
| Framework standards | check official docs for expected coverage | Required topics for the stack |

### 3. Gap identification

Compare baseline vs needs. Classify every topic into exactly one category:

| Category | Definition | Example |
|---|---|---|
| **Missing** | Required topic, no page exists | No deployment guide for a deployable app |
| **Thin** | Page exists but < 200 words or missing code examples | API auth page with no request samples |
| **Redundant** | 2+ pages covering the same topic | Three separate "getting started" guides |
| **Outdated** | Content references deprecated APIs or old versions | v1 examples when v3 is current |

### 4. Prioritized recommendations

Score each gap by `impact × effort`:

| Impact | Effort | Priority |
|---|---|---|
| High (blocks users) | Low (< 1 hour) | P1 — do first |
| High | High | P2 — plan sprint |
| Low | Low | P3 — quick win |
| Low | High | P4 — backlog |

**Verify:** every recommendation references a specific file path or topic name from step 1.

## Output format

Produce a `GAP_ANALYSIS_REPORT.md` with this structure:

```markdown
# Gap Analysis: <project name>

## Summary
- Total pages: N
- Missing topics: N
- Thin pages: N
- Redundant sets: N
- Outdated pages: N

## Missing Topics (P1/P2)
| Topic | Why needed | Priority | Suggested location |
|---|---|---|---|

## Thin Pages
| File | Current words | What's missing |
|---|---|---|

## Consolidation Targets
| Pages to merge | Into | Reason |
|---|---|---|

## Outdated Content
| File | Issue | Fix |
|---|---|---|

## Roadmap
1. ...
2. ...
```
