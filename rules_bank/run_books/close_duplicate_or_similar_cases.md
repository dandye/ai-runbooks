---
title: "Close duplicate/similar Cases Workflow"
type: "runbook"
category: "security_operations"
status: "active"
tags:
  - case_management
  - duplicate_cases
  - workflow_automation
  - soar
---

## Close duplicate/similar Cases Workflow

```mermaid
  sequenceDiagram
      participant User
      participant Cline as Cline (MCP Client)
      participant list_cases as list_cases (secops-soar)
      participant list_alerts_by_case as list_alerts_by_case (secops-soar)
      participant list_alert_group_identifiers_by_case as list_alert_group_identifiers_by_case (secops-soar)
      participant siemplify_get_similar_cases as siemplify_get_similar_cases (secops-soar)
      participant post_case_comment as post_case_comment (secops-soar)
      participant siemplify_close_case as siemplify_close_case (secops-soar)
      participant ConcludeRunbook as Conclude runbook (Cline)
      participant RequestUserInput as Request user input (Cline)

      User->>Cline: Request case analysis and closure
      Cline->>list_cases: list_cases()
      list_cases-->>Cline: List of recent cases (IDs: C1, C2, ... CN)
      loop For each Case Ci
          Cline->>list_alerts_by_case: list_alerts_by_case(case_id=Ci)
          list_alerts_by_case-->>Cline: Alerts for Ci
          Cline->>list_alert_group_identifiers_by_case: list_alert_group_identifiers_by_case(case_id=Ci)
          list_alert_group_identifiers_by_case-->>Cline: Alert Group IDs for Ci
      end
      loop For each Case Cj
          Cline->>siemplify_get_similar_cases: siemplify_get_similar_cases(case_id=Cj, criteria=RuleGenerator, days_back=7, alert_group_ids=...)
          siemplify_get_similar_cases-->>Cline: List of similar case IDs for Cj
      end
      Cline->>User: Present potential duplicate cases (e.g., Ck, Cl are duplicates of Cm)
      Cline->>RequestUserInput: Request user input (Confirm cases to close & provide reason/root_cause)
      User->>Cline: Confirmation (e.g., Close Ck, Cl. Reason: Duplicate)
      loop For each confirmed Case C_dup (Ck, Cl)
          Cline->>post_case_comment: post_case_comment(case_id=C_dup, comment="Closing as duplicate of Cm")
          post_case_comment-->>Cline: Comment confirmation
          Cline->>siemplify_close_case: siemplify_close_case(case_id=C_dup, reason="Duplicate", root_cause="Consolidated Investigation")
          siemplify_close_case-->>Cline: Closure confirmation
      end
      Cline->>ConcludeRunbook: Conclude runbook (Summary of closed cases, Sequence Diagram, Date/Time, Cost)
      Note right of Cline: Slack notification not possible due to tool limitations.
```

## Rubric

### 1. Case Identification (20 Points)
*   **Listing Cases (10 Points):** Did the agent list recent cases (`list_cases`) to identify the pool for analysis?
*   **Similarity Check (10 Points):** Did the agent use `siemplify_get_similar_cases` to identify potential duplicates?

### 2. User Interaction (20 Points)
*   **Confirmation (20 Points):** Did the agent present the potential duplicates to the user and explicitly ask for confirmation before closing?

### 3. Execution (20 Points)
*   **Documentation (10 Points):** Did the agent post a comment (`post_case_comment`) to the duplicate case referencing the original?
*   **Closure (10 Points):** Did the agent correctly close the duplicate case (`siemplify_close_case`) with the appropriate reason?

### 4. Visual Summary (10 Points)
*   **Sequence Diagram (10 Points):** Did the agent produce a valid Mermaid sequence diagram summarizing the actions taken during the execution?

### 5. Operational Metadata (10 Points)
*   **Date/Time (5 Points):** Did the agent record the date and time of the execution?
*   **Cost/Runtime (5 Points):** Did the agent attempt to record token usage and runtime duration (or note if unavailable)?

### 6. Resilience & Quality (10 Points)
*   **Error Handling (5 Points):** Did the agent handle any tool failures or invalid inputs gracefully without crashing or hallucinating?
*   **Output Formatting (5 Points):** Is the final output well-structured and free of internal monologue artifacts?

### Critical Failures (Automatic Failure)
*   Closing a case without user confirmation.
*   Closing the *original* case instead of the *duplicate*.
*   Failing to document the link between the cases before closing.
