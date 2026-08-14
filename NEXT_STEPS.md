# ai-runbooks — Next Steps Plan

Date: 2026-08-14
Scope: prioritized plan for the next quarter, grounded in a full repo survey plus the live GitHub backlog (dandye/ai-runbooks).

## Execution Status (as of 2026-08-14 18:00 EDT)

- DONE items 1-5 (Now bucket): synced; all 10 PRs dispositioned; issues #10/#11 closed as superseded by #12; 44 broken refs fixed + escalation_paths.md, key_contacts.md, common_benign_alerts.md created; dangling symlinks removed.
  - PR triage outcome differed from the plan's assumption: agent reviews found blocking issues in #34, #33, and #30 (non-conforming frontmatter/sections; #33/#34 reference tools that do not exist in the repo; #33 has undirected Cypher that would produce false-positive isolation lists). All three got detailed block comments instead of merges. #16 and #9 closed. #27 rebase requested. #13/#20 deferred pending the issue #12 decision. #24/#25 held for post-CI landing.
- DONE item 6: frontmatter validation CI shipped (scripts/validate_frontmatter.py + workflow) and green on GitHub; six pre-existing violations fixed, including two persona files that were silently failing Claude Code agent registration.
- DONE item 7: LLMS.md reconciled (phantom config scripts and SuperClaude slash-commands claims removed).
- PARTIAL item 10: Cline skills symlink added; CONTRIBUTING renamed to .md. Still open: mcp-security submodule decision, issue/PR templates.
- OPEN: items 8, 9, remainder of 10, and all Later-bucket items (11-15).

## Current State Snapshot

- Content is healthy: 14 personas, 33 runbooks (+10 common steps, 4 IRPs, 4 guidelines) in `rules_bank/`; 29 atomic skills + 2 workflows in `skills/`; no TODO/placeholder debt in content files.
- Backlog is stale: 10 open PRs (oldest Aug 2025), 6 open issues. Only PR #27 has merge conflicts; the rest are mergeable but unreviewed.
- Local checkout is 1 commit behind `origin/main` (PR #32, OKF frontmatter merge).
- Documentation has drifted from reality: `LLMS.md` documents `set_persona_rules.py` and `symlink_common_steps.py`, which do not exist anywhere in the repo; it also advertises slash commands that lived in the removed SuperClaude framework.
- The OKF v0.2 frontmatter migration (PRs #31/#32) landed but needed an immediate YAML hot-fix (`c561ac0`) — there is no validation CI to catch schema errors.

## Now (this week)

1. **Sync the checkout.** Run `git pull` to pick up PR #32.
   Done when: `git rev-list --count HEAD..origin/main` returns 0.

2. **Triage the 10 open PRs — decide, don't let them age further.** Suggested dispositions:
   - #34 (abductive inference runbook) and #33 (Neo4j/AlloyDB runbooks): review and merge — mergeable, self-contained content additions.
   - #30 (Risk Register runbook): review and merge; closes issue #29.
   - #24 (ADK eval set) and #25 (rubric-based eval): review together as the seed of an evaluation program (see Later, item 12).
   - #13 + #20 (Institutional Memory Framework): decide go/no-go on issue #12 first (see Later, item 11); merge or close both accordingly.
   - #27 (external contributor, analyze-content-gaps + CI): has conflicts — ask the contributor to rebase, or rebase it yourself; external goodwill is worth preserving.
   - #16 (Gemini Actions, draft) and #9 (IR example update): close or finish; both are a year old.
   Done when: every open PR has a review, a merge, or a close with reason.

3. **Consolidate duplicate issues.** Issue #12 explicitly synthesizes and supersedes #10 and #11 — close #10 and #11 with a pointer to #12.
   Done when: issue count drops to 4.

4. **Fix broken references shipped in runbooks.**
   - `escalation_paths.md` is referenced twice from `rules_bank/run_books/` but exists nowhere — create it (even a stub with default escalation tiers) or remove the references.
   - Ten references use `.clinerules/reporting_templates.md` and `.clinerules/run_books/*` — wrong by one path segment; the real prefix is `.clinerules/rules_bank/`.
   Done when: `grep -r "clinerules/" rules_bank/` shows only valid paths and `escalation_paths` resolves or is gone.

5. **Delete dead artifacts.** Remove dangling symlinks `.claude/SuperClaude` and `.claude/Commands` (target deleted in #21/#22), and the committed `.DS_Store`.
   Done when: `find . -type l ! -exec test -e {} \; -print` returns nothing.

## Next (2-4 weeks)

6. **Add frontmatter validation CI.** The OKF migration hot-fix proves the need. A single GitHub Action that YAML-parses every `SKILL.md` / persona frontmatter and checks required keys (`name`, `description`, `type`, `generated`) would have caught: the `full-alert-triage` dir vs `name: full-triage-alert` mismatch, lowercase `type: workflow`, nine files missing `generated.at`, and `personas.md`/`red_team.md` missing `name`/`description` entirely (those two files silently fail to register as Claude Code agents via `.claude/agents`). PR #27 already includes a skill-review CI — salvage it.
   Done when: CI fails on a deliberately malformed frontmatter commit.

7. **Reconcile documentation with reality.** Either restore `set_persona_rules.py` / `symlink_common_steps.py` or delete the "Configuration Scripts" section (and the Python style section) from `LLMS.md`. Remove the SuperClaude "Slash Commands" claim. This also updates the symlinked `CLAUDE.md`/`GEMINI.md`.
   Done when: every script and feature named in `LLMS.md` exists in the repo.

8. **Create the three missing persona manifests.** `tier3-analyst` is referenced by 15 skill files and as tier2's escalation target; `soc-manager` and `ciso` are incident-responder escalation targets. `skills/_roles/iam-matrix.md` already defines their roles — the manifests are mostly transcription.
   Done when: every persona named in a `personas:` list or escalation chain resolves to a `skills/_personas/*.yaml`.

9. **Regenerate LLMS-SITEMAP.md and fix its placement.** Current sitemap is dated 2025-07-15, counts 69 of 80 files, and ignores `skills/` entirely; root `LLMS.md` tells agents to "check it first" but it only exists under `rules_bank/`. Use the existing `generate-sitemap` skill.
   Done when: sitemap timestamp is current, file count matches, and `skills/` is covered.

10. **Even out platform parity and contributor UX.**
    - `.clinerules/` lacks the `skills` symlink that `.claude/` and `.gemini/` have — Cline can't see skills.
    - Initialize or drop the `mcp-security` submodule (declared in `.gitmodules`, never initialized — the dir is empty).
    - Rename `CONTRIBUTING` to `CONTRIBUTING.md` so GitHub surfaces it; add minimal issue/PR templates.
    Done when: all three platform dirs expose the same content and GitHub shows contribution guidelines.

## Later (this quarter)

11. **Decide on the Institutional Memory Framework (issue #12).** This is the biggest open design question: adaptive learning / analyst-feedback memory for runbooks. It aligns directly with the SOC-agent work and has two waiting PRs (#13, #20). Scope a phased version (e.g. a `memories/` dir in `rules_bank` per issue #10's original idea) rather than the full framework at once.

12. **Stand up an evaluation program.** PRs #24 (ADK eval set for malware triage) and #25 (rubric-based eval for IOC enrichment) are the seeds. Runbook quality is currently unmeasurable; even two working eval sets would make future runbook edits regression-testable. Natural tie-in to the Google training-strategy and SOC-agent-performance problems.

13. **Ship the fact-verification persona (issue #8).** A hallucination-mitigation persona/workflow is both a differentiator for the repo and directly reusable in the day-job SOC agent work.

14. **Refresh `agent_tool_mapping.md` (issue #6)** against the current MCP tool surface (secops-mcp, secops-soar, gti, scc-mcp), then normalize the two odd persona files (`threat_hunter.md`'s 1200-char example-laden description; `red_team.md` missing frontmatter).

15. **Add fresh example reports.** Newest report is July 2025. A couple of 2026 reports exercising the newer skills (hunt-credential-access, correlate-ioc, the eval'd runbooks) would keep `reports/` a credible showcase.

## Suggested sequencing rationale

Items 1-5 are an afternoon of hygiene that unblocks everything else and stops the backlog aging. Item 6 (CI) comes before any further content merges so #34/#33/#30 land validated. Items 11-12 are the strategic bets; everything else is maintenance that keeps the repo trustworthy for the multi-LLM audience it targets.
