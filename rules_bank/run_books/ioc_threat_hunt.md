---
title: "Runbook: IOC Threat Hunt"
type: "runbook"
category: "security_operations"
status: "active"
tags:
  - ioc_hunting
  - threat_hunting
  - indicators
  - proactive_hunting
---

# Runbook: IOC Threat Hunt

## Objective

To proactively hunt for specific Indicators of Compromise (IOCs) across the environment based on threat intelligence feeds, recent incidents, emerging threats, or specific hypotheses. This runbook enables systematic searching for known bad indicators to identify potential compromise, lateral movement, or persistence mechanisms that may have evaded detection rules.

## Scope

Focuses on searching SIEM and data lake sources for specific IOC values (IPs, domains, file hashes, URLs) using targeted queries optimized for each IOC type. Includes basic enrichment of findings, correlation with existing cases, and escalation procedures for confirmed hits. Covers multiple IOC types in a single hunt session and provides comprehensive documentation of hunt methodology and results. Excludes hypothesis-driven hunting or advanced analytics - those are covered by specialized threat hunting runbooks.

## Inputs

*   `${IOC_LIST}`: Comma-separated list of IOC values to hunt for.
*   `${IOC_TYPES}`: Corresponding comma-separated list of IOC types (e.g., "IP Address, Domain, File Hash").
*   `${HUNT_TIMEFRAME_HOURS}`: Lookback period in hours (e.g., 72, 168; Use 96 as default).
*   *(Optional) `${HUNT_CASE_ID}`: SOAR case ID for tracking.*
*   *(Optional) `${REASON_FOR_HUNT}`: Brief description why these IOCs are being hunted.*

## Tools

*   `secops-mcp`: `search_security_events`, `lookup_entity`, `get_ioc_matches`
*   `gti-mcp`: (Relevant enrichment tools like `get_ip_address_report`, `get_domain_report`, etc.)
*   `secops-soar`: `post_case_comment` (for documenting hunt/findings)

## Workflow Steps & Diagram

1.  **Receive Inputs:** Obtain `${IOC_LIST}`, `${IOC_TYPES}`, `${HUNT_TIMEFRAME_HOURS}`, etc.
2.  **Create Hunt Todo List:** For systematic tracking, create a todo list following `common_steps/todo_list_generation.md`. Include tasks for each IOC to be hunted, enrichment steps, and reporting. Display the initial list to show hunt scope.
3.  **Initial Check (Optional):** Use `secops-mcp.get_ioc_matches` to see if any IOCs in the list have recent matches in the SIEM's integrated feeds.
4.  **Iterative SIEM Search:**
    *   For each IOC in `${IOC_LIST}`:
        *   Construct appropriate UDM queries for `secops-mcp.search_security_events` based on the IOC value and type.
        *   Execute the search over `${HUNT_TIMEFRAME_HOURS}` (or use 96 by default).
        *   Analyze results for any hits (e.g., network connections, file executions, DNS lookups).
5.  **Enrich Findings:**
    *   If hits are found for an IOC:
        *   Use `secops-mcp.lookup_entity` for the IOC and any involved entities (hosts, users).
        *   Use relevant `gti-mcp` tools to enrich the IOC itself.
6.  **Document Hunt & Findings:**
    *   Use `secops-soar.post_case_comment` in `${HUNT_CASE_ID}` (if provided) or a dedicated hunt case.
    *   Document: IOCs Hunted, Timeframe, Queries Used, Summary of Findings (including IOCs with no hits), Details of any confirmed hits and enrichment data.
7.  **Escalate or Conclude:**
    *   If confirmed malicious activity related to the hunted IOCs is found, escalate by creating/updating an incident case.
    *   If no significant findings, conclude the hunt and document it.
    *   **Action:** Generate a Mermaid sequence diagram summarizing the specific actions taken during this execution.
    *   **Action:** Record the current date and time of execution.
    *   **Action:** (Optional) Record the token usage and runtime duration if available from the environment.

```mermaid
sequenceDiagram
    participant Analyst/Hunter
    participant Cline as Cline (MCP Client)
    participant SIEM as secops-mcp
    participant GTI as gti-mcp
    participant SOAR as secops-soar

    Analyst/Hunter->>Cline: Start IOC Threat Hunt\nInput: IOC_LIST, IOC_TYPES, HUNT_TIMEFRAME_HOURS, ...

    %% Step 2: Initial Check (Optional)
    opt Check IOC Matches
        Cline->>SIEM: get_ioc_matches(hours_back=HUNT_TIMEFRAME_HOURS)
        SIEM-->>Cline: Recent IOC Matches
        Note over Cline: Correlate with IOC_LIST
    end

    %% Step 3: Iterative SIEM Search
    loop For each IOC Ii in IOC_LIST
        Note over Cline: Construct UDM query Qi for Ii
        Cline->>SIEM: search_security_events(text=Qi, hours_back=HUNT_TIMEFRAME_HOURS)
        SIEM-->>Cline: Search Results for Ii
        Note over Cline: Analyze results for hits
    end

    %% Step 4: Enrich Findings
    opt Hits Found for IOC Ij (Involved Entities E1, E2...)
        Cline->>SIEM: lookup_entity(entity_value=Ij)
        SIEM-->>Cline: SIEM Summary for Ij
        Cline->>GTI: get_..._report(ioc=Ij)
        GTI-->>Cline: GTI Enrichment for Ij
        loop For each Involved Entity Ek (E1, E2...)
            Cline->>SIEM: lookup_entity(entity_value=Ek)
            SIEM-->>Cline: SIEM Summary for Ek
        end
    end

    %% Step 5: Document Hunt
    Cline->>SOAR: post_case_comment(case_id=HUNT_CASE_ID, comment="IOC Hunt Summary: IOCs [...], Findings [...], Enrichment [...]")
    SOAR-->>Cline: Comment Confirmation

    %% Step 6: Escalate or Conclude
    alt Confirmed Activity Found
        Note over Cline: Escalate findings (Create/Update Incident Case)
        Cline->>Analyst/Hunter: Conclude runbook (result="IOC Hunt complete. Findings escalated.")
    else No Significant Findings
        Cline->>Analyst/Hunter: Conclude runbook (result="IOC Hunt complete. No significant findings. Hunt documented.")
    end
```

## Completion Criteria

- All provided IOCs searched across specified timeframe using appropriate UDM queries
- IOC match check completed against integrated threat intelligence feeds
- Search results analyzed for legitimate vs. suspicious activity patterns
- Any hits enriched using GTI and SIEM entity lookup capabilities
- Involved entities (hosts, users, processes) identified and assessed for impact
- Correlation performed with existing open cases and previous incidents
- Hunt findings documented in SOAR with detailed methodology and results
- Confirmed malicious activity escalated to incident response processes
- Hunt summary includes both positive and negative results for intelligence value
- IOCs with no hits documented to confirm environment is clean
- Recommendations provided for detection rule improvements or monitoring gaps

## Expected Outputs

- **Hunt Results Summary**: Comprehensive overview of all IOCs searched and findings
- **Hit Analysis**: Detailed breakdown of any confirmed IOC matches with context
- **Entity Impact Assessment**: Analysis of compromised or affected systems/users
- **Timeline Reconstruction**: Sequence of events for any confirmed malicious activity
- **SOAR Documentation**: Case comments with complete hunt methodology and findings
- **Escalation Actions**: Incident cases created or updated for confirmed threats
- **Clean IOCs List**: Documentation of IOCs with no environmental presence
- **Detection Gaps**: Recommendations for improved monitoring or detection rules
- **Workflow Documentation**: Sequence diagram showing actual MCP tools and servers used during execution
- **Runbook Reference**: Clear identification of which runbook was executed to generate the report
- **Todo List Tracking**: Final status of all hunt tasks with completion percentage

## Rubric

### 1. Scope & Strategy (15 Points)
*   **IOC Parsing (5 Points):** Did the agent correctly parse and list all IOCs to be hunted?
*   **Initial Check (10 Points):** Did the agent perform a preliminary check (`get_ioc_matches`)?

### 2. Search Execution (25 Points)
*   **Query Construction (15 Points):** Did the agent construct valid UDM queries for each IOC?
*   **Iterative Search (10 Points):** Did the agent loop through the IOC list and execute searches for all targets?

### 3. Analysis & Enrichment (20 Points)
*   **Hit Analysis (10 Points):** Did the agent analyze search hits for validity (TP/FP)?
*   **Enrichment (10 Points):** Did the agent enrich confirmed hits?

### 4. Reporting (10 Points)
*   **Documentation (10 Points):** Did the agent document the hunt results, including negative findings, in the case?

### 5. Visual Summary (10 Points)
*   **Sequence Diagram (10 Points):** Did the agent produce a valid Mermaid sequence diagram summarizing the actions taken during the execution?

### 6. Operational Metadata (10 Points)
*   **Date/Time (5 Points):** Did the agent record the date and time of the execution?
*   **Cost/Runtime (5 Points):** Did the agent attempt to record token usage and runtime duration (or note if unavailable)?

### 7. Resilience & Quality (10 Points)
*   **Error Handling (5 Points):** Did the agent handle any tool failures or invalid inputs gracefully without crashing or hallucinating?
*   **Output Formatting (5 Points):** Is the final output well-structured and free of internal monologue artifacts?

### Critical Failures (Automatic Failure)
*   Failing to search for all provided IOCs.
*   Documenting a "clean" hunt when there were obvious search hits.
*   Searching over an incorrect timeframe (e.g., 1 hour instead of 72).
