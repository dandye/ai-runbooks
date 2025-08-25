

# Feature Proposal: Adaptive Learning Framework for AI Runbooks

This document reframes the original "Adaptive Learning" proposal into an actionable implementation plan that aligns with the existing `rules_bank` and `personas` structure.

## Core Concept: From Static Runbooks to Dynamic Institutional Memory

The goal is to create a system where the agent can learn from analyst feedback and operational experience to improve its execution of runbooks. This moves beyond static procedures to a dynamic system that adapts to our organization's unique security context. We will call this `Institutional Memory`.

## Proposed Structure

We will introduce a new directory: `rules_bank/memories/`. This directory will store the learned procedures and context.

### Memory File Format

Each file within `rules_bank/memories/` will be a Markdown file representing a single "memory." The filename will correspond to the runbook it modifies, with a persona-specific suffix.

**Example Filename:** `triage_alerts_soc_analyst_tier_1.md`

**File Content:**

```markdown
---
runbook: "run_books/triage_alerts.md"
persona: "personas/soc_analyst_tier_1.md"
source_step: "Step 3: IOC Enrichment"
confidence: 0.95
last_updated: "2025-08-23"
---

## Analyst Feedback

"For our organization, when triaging alerts from the 'XYZ' sensor, we must always perform a historical lookup in our internal 'ThreatDB' before proceeding with public enrichment. This is a critical step that is currently missing."

## Original Procedure (for context)

- **Tool:** `secops-mcp enrich_ioc`
- **Parameters:** `ioc={ioc_value}`

## Derived Procedure

1.  **Internal Enrichment:**
    - **Tool:** `internal_db query`
    - **Parameters:** `database=ThreatDB, query={ioc_value}`
2.  **Conditional Public Enrichment:**
    - **Condition:** If internal enrichment returns no results.
    - **Tool:** `secops-mcp enrich_ioc`
    - **Parameters:** `ioc={ioc_value}`

## Application Log

- **2025-08-23:** Memory created based on feedback from analyst 'D. Anderson'.
- **2025-08-24:** Procedure successfully applied to Alert #4512.
```

## Workflow

1.  **Initiation:** An agent, operating under a specific persona (e.g., `soc_analyst_tier_1`), is tasked with executing a runbook (e.g., `triage_alerts.md`).

2.  **Memory Check:** Before executing a step in the runbook, the agent checks the `rules_bank/memories/` directory for a corresponding memory file (e.g., `triage_alerts_soc_analyst_tier_1.md`).

3.  **Procedure Proposal:** If a relevant, high-confidence memory is found, the agent presents the "Derived Procedure" to the analyst as the recommended course of action for that step.

4.  **Analyst Interaction & Feedback:**
    - The analyst can **approve** the derived procedure, and the agent executes it.
    - The analyst can **reject** it and proceed with the original runbook step.
    - The analyst can provide **new feedback** in natural language (e.g., "That's close, but for this specific alert type, also check the 'LogRepo' system.").

5.  **Memory Formation/Update:**
    - New feedback is processed by a meta-agent.
    - A new memory file is created, or an existing one is updated. The `confidence` score may be adjusted based on the feedback. The `Application Log` is updated.

## Benefits

*   **Context-Aware Execution:** Aligns agent behavior with our organization's specific operational realities.
*   **Structured Learning:** Creates a clear, auditable trail of how and why procedures are evolving.
*   **Analyst-Driven:** Empowers the security team to directly shape and improve the agent's capabilities without needing to edit the core runbooks.
*   **Dynamic Expertise:** Transforms static runbooks into a dynamic knowledge base that represents our collective `Institutional Memory`.
