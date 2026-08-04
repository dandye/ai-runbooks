---
type: "Playbook"
title: "AlloyDB Multi-Modal Vector Similarity Investigation Grounding"
description: "Procedure for querying historical Chronicle detection reports and investigation verdicts in AlloyDB using 768-dim text-embedding-004 vector embeddings."
resource: "ai-runbooks/rules_bank/run_books/alloydb_vector_similarity_investigation_grounding.md"
timestamp: "2026-08-04T17:44:38Z"
provenance:
  source_type: "manual"
  source_tool: "Antigravity"
  timestamp: "2026-08-04T17:44:38Z"
---

# AlloyDB Multi-Modal Vector Similarity Investigation Grounding

## Objective

Provide clear operational guidelines for SOC agents to query historical Chronicle detection reports and past incident verdicts in AlloyDB. This grounding enables agents to leverage historical threat patterns, eliminate redundant SIEM searches, and ground containment recommendations on verified past verdicts.

## Scope

This runbook applies to Tier 1 Analyst, Threat Hunter, and Orchestrator agents when evaluating incoming security alerts or conducting investigative HANDOFFS where historical case context is required.

## Inputs

*   `${QUERY_TEXT}`: Search string containing technical indicators, TTP behaviors, or command-line patterns (e.g., `"powershell download cradle"`, `"MSBuildShell execution"`).
*   `${SEMANTIC_FLAG}`: Set to `True` for 768-dim vector embedding similarity search, or `False` for exact full-text/metadata SQL matching.
*   `${PROFILE_NAME}`: Similarity scoring profile (`threat-hunt`, `incident-response`, `detection-engineering`).
*   `${TOP_K}`: Number of top matching reports to retrieve (default: 5).

## Tools Used

*   `alloydb-mcp`: `query_alloydb_detection_reports` (`AlloyDBManager.search`).
*   `secops-soar`: `save_report_artifact`.

---

## Dual-Mode Search Strategy

### 1. Semantic Vector Search (`semantic=True`)
Use semantic vector search when querying:
* Abstract attack TTPs or behavioral concepts (e.g., `"unusual parent-child process relationship"`, `"suspicious credential dumping via memory access"`).
* Polymorphic threat behaviors where exact file names or command-line strings may vary between campaigns.
* Conceptual similarity across past investigation verdicts.

### 2. Metadata SQL Search (`semantic=False`)
Use exact metadata SQL search when querying:
* Specific Investigation IDs (e.g., `INV-2026-0801-0042`).
* Exact IOC values (e.g., SHA256 hashes, IP addresses, domain names).
* Standard verdict categories (e.g., `verdict = "TRUE_POSITIVE"`).

---

## Scoring Profiles & Weight Distributions

| Profile Name | Vector Similarity Weight | Entity Overlap Weight | Verdict Confidence Weight | Primary Use Case |
| :--- | :---: | :---: | :---: | :--- |
| **`threat-hunt`** | 60% | 30% | 10% | Proactive TTP discovery and behavioral pattern matching. |
| **`incident-response`** | 30% | 50% | 20% | Entity blast radius correlation and containment validation. |
| **`detection-engineering`** | 40% | 30% | 30% | Rule false-positive tuning and alert signature verification. |

---

## Workflow Steps

### Step 1: Query Construction & Strategy Selection
1. Parse incoming alert telemetry for key TTPs, command-line arguments, or process trees.
2. Determine whether the query requires semantic vector search or exact SQL filtering.

### Step 2: AlloyDB Search Execution (`query_alloydb_detection_reports`)
1. Invoke `query_alloydb_detection_reports` with the selected parameters:
   ```json
   {
     "query": "powershell download cradle",
     "semantic": true,
     "profile": "threat-hunt",
     "limit": 5
   }
   ```
2. If vector search returns relevant historical detection reports:
   * Extract historical verdicts, verified root causes, and containment steps.
   * Cite historical investigation IDs (e.g., `INV-...`) in the reasoning transcript.
3. If no matching reports are found:
   * Fall back to live SIEM log search (`search_security_events`).

### Step 3: Synthesis & Remediation Grounding
1. Compare current alert context against retrieved historical report verdicts.
2. Incorporate proven remediation steps into current Tier 2 containment recommendations.
3. Save structured analysis using `save_report_artifact`.
