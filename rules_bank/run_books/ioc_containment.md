---
title: "IOC Containment Runbook"
type: "runbook"
category: "security_operations"
status: "active"
tags:
  - ioc_containment
  - incident_response
  - containment
  - threat_mitigation
---

# IOC Containment Runbook

## Objective

Quickly execute containment actions for identified malicious Indicators of Compromise (IOCs) such as IP addresses, domains, or file hashes, leveraging available SIEM, SOAR, GTI, and potentially EDR/Firewall tools.

## Scope

This runbook focuses on the immediate containment actions based on confirmed malicious IOCs. It assumes the IOCs have been identified through prior investigation (e.g., alert triage, threat hunting, GTI research).

## Inputs

*   `${IOC_VALUE}`: The specific IOC value (e.g., "198.51.100.10", "evil-domain.com", "abcdef123456...").
*   `${IOC_TYPE}`: The type of IOC (e.g., "IP Address", "Domain", "File Hash").
*   `${CASE_ID}`: The relevant SOAR case ID for documentation.
*   `${ALERT_GROUP_IDENTIFIERS}`: Relevant alert group identifiers from the SOAR case.

## Tools

*   `gti-mcp`: `get_ip_address_report`, `get_domain_report`, `get_file_report` (Optional: for final reputation check)
*   `secops-soar`: `google_chronicle_add_values_to_reference_list` (Example: for adding to SIEM blocklist)
*   `secops-soar`: `post_case_comment` (For documentation)
*   *(Potentially other SOAR actions for specific integrations like Firewalls, Proxies, EDR)*
*   `secops-mcp`: `search_security_events` (To find related activity/endpoints for file hashes)
*   **Action:** Request user input (e.g., using `ask_followup_question` to confirm actions)

## Workflow Steps & Diagram

1.  **Receive Input:** Obtain `${IOC_VALUE}`, `${IOC_TYPE}`, `${CASE_ID}`, and `${ALERT_GROUP_IDENTIFIERS}`.
2.  **(Optional) Final Reputation Check:** Use the appropriate `gti-mcp` tool (`get_ip_address_report`, `get_domain_report`, `get_file_report`) for `${IOC_VALUE}` to confirm malicious reputation before blocking.
3.  **Confirm Containment Action:** Execute `common_steps/confirm_action.md` with `QUESTION_TEXT="Proceed with containment for ${IOC_VALUE} (${IOC_TYPE})?"` and `RESPONSE_OPTIONS=["Yes", "No"]`. Obtain `${USER_RESPONSE}`.
4.  **Execute Containment (If Confirmed):**
    *   If `${USER_RESPONSE}` is "Yes":
        *   **If `${IOC_TYPE}` is IP Address or Domain:**
            *   Add `${IOC_VALUE}` to the appropriate blocklist reference list in Chronicle SIEM using `secops-soar.google_chronicle_add_values_to_reference_list`. (Requires knowing the correct `reference_list_name`, e.g., "IP_Blocklist", "Domain_Blocklist"). Let the action status be `CONTAINMENT_ACTION_STATUS`.
            *   *(Optional: Execute actions via specific Firewall/Proxy SOAR integrations if available)*.
        *   **If `${IOC_TYPE}` is File Hash:**
            *   Search SIEM (`secops-mcp.search_security_events`) for events involving the file hash (`target.file.md5 = "${IOC_VALUE}"` or similar) to identify affected endpoints.
            *   *(Optional: Execute EDR actions like file quarantine/deletion on identified endpoints via specific EDR SOAR integrations if available)*. Let the action status be `CONTAINMENT_ACTION_STATUS`.
        *   **Document Action:** Execute `common_steps/document_in_soar.md` with `${CASE_ID}` and `COMMENT_TEXT="Containment action attempted for IOC: ${IOC_VALUE} (Type: ${IOC_TYPE}). Action: [Blocked/EDR Action Attempted]. Status: ${CONTAINMENT_ACTION_STATUS}"`. Obtain `${COMMENT_POST_STATUS}`.
    *   If `${USER_RESPONSE}` is "No":
        *   **Document Action:** Execute `common_steps/document_in_soar.md` with `${CASE_ID}` and `COMMENT_TEXT="Containment action aborted by analyst for IOC: ${IOC_VALUE} (Type: ${IOC_TYPE})."`. Obtain `${COMMENT_POST_STATUS}`.
5.  **Completion:** Conclude the runbook execution.

```mermaid
sequenceDiagram
    participant Analyst
    participant Cline as Cline (MCP Client)
    participant GTI as gti-mcp
    participant ConfirmAction as common_steps/confirm_action.md
    participant SOAR as secops-soar
    participant SIEM as secops-mcp
    participant DocumentInSOAR as common_steps/document_in_soar.md
    %% EDR/Firewall conceptual participants
    participant EDR as EDR (Conceptual)
    participant Firewall as Firewall (Conceptual)

    Analyst->>Cline: Start IOC Containment Runbook\nInput: IOC_VALUE, IOC_TYPE, CASE_ID, ALERT_GROUP_IDS

    %% Step 2: Optional Reputation Check
    opt Reputation Check
        alt IOC_TYPE is IP Address
            Cline->>GTI: get_ip_address_report(ip_address=IOC_VALUE)
            GTI-->>Cline: IP Report (Confirm Malicious)
        else IOC_TYPE is Domain
            Cline->>GTI: get_domain_report(domain=IOC_VALUE)
            GTI-->>Cline: Domain Report (Confirm Malicious)
        else IOC_TYPE is File Hash
            Cline->>GTI: get_file_report(hash=IOC_VALUE)
            GTI-->>Cline: File Report (Confirm Malicious)
        end
    end

    %% Step 3: Confirm Action
    Cline->>ConfirmAction: Execute(Input: QUESTION_TEXT="Proceed...?", RESPONSE_OPTIONS=["Yes", "No"])
    ConfirmAction-->>Cline: Results: USER_RESPONSE

    %% Step 4: Execute Containment (If Confirmed)
    alt USER_RESPONSE is "Yes"
        Note over Cline: Containment_Action_Status = "Attempted"
        alt IOC_TYPE is IP Address or Domain
            Note over Cline: Determine Reference List Name (e.g., "IP_Blocklist")
            Cline->>SOAR: google_chronicle_add_values_to_reference_list(case_id=CASE_ID, ..., values=IOC_VALUE)
            SOAR-->>Cline: Blocklist Add Result -> Update Containment_Action_Status
            opt Firewall/Proxy Integration Available
                 Cline->>Firewall: (Conceptual) Block IOC_VALUE
                 Firewall-->>Cline: Block Result -> Update Containment_Action_Status
            end
        else IOC_TYPE is File Hash
            Cline->>SIEM: search_security_events(text="Events with hash IOC_VALUE")
            SIEM-->>Cline: Events (Identify Endpoints E1, E2...)
            opt EDR Integration Available
                loop For each Endpoint Ei
                    Cline->>EDR: (Conceptual) Quarantine/Delete Hash IOC_VALUE on Ei
                    EDR-->>Cline: EDR Action Result -> Update Containment_Action_Status
                end
            else
                Note over Cline: Containment_Action_Status = "Manual EDR Action Needed"
            end
        end

        %% Document Action (Yes case)
        Cline->>DocumentInSOAR: Execute(Input: CASE_ID, COMMENT_TEXT="Containment action attempted...")
        DocumentInSOAR-->>Cline: Results: COMMENT_POST_STATUS
        Cline->>Analyst: Conclude runbook (result="IOC Containment runbook complete for IOC_VALUE. Action attempted.")

    else USER_RESPONSE is "No"
         %% Document Action (No case)
         Cline->>DocumentInSOAR: Execute(Input: CASE_ID, COMMENT_TEXT="Containment action aborted...")
         DocumentInSOAR-->>Cline: Results: COMMENT_POST_STATUS
         Cline->>Analyst: Conclude runbook (result="IOC Containment runbook aborted for IOC_VALUE.")
    end

## Runbook Conclusion
*   **Action:** Generate a Mermaid sequence diagram summarizing the specific actions taken during this execution.
*   **Action:** Record the current date and time of execution.
*   **Action:** (Optional) Record the token usage and runtime duration if available from the environment.
*   Conclude the runbook execution.

## Rubric

### 1. Reputation Verification (20 Points)
*   **Check (20 Points):** Did the agent perform a final reputation check (GTI) before containment?

### 2. Containment Logic (30 Points)
*   **Confirmation (15 Points):** Did the agent explicitly ask the user for confirmation?
*   **Execution (15 Points):** Did the agent execute the correct containment action (e.g., blocklist add) only *after* confirmation?

### 3. Documentation (20 Points)
*   **Log (20 Points):** Did the agent document the action taken (or aborted) in the case?

### 4. Visual Summary (10 Points)
*   **Sequence Diagram (10 Points):** Did the agent produce a valid Mermaid sequence diagram summarizing the actions taken during the execution?

### 5. Operational Metadata (10 Points)
*   **Date/Time (5 Points):** Did the agent record the date and time of the execution?
*   **Cost/Runtime (5 Points):** Did the agent attempt to record token usage and runtime duration (or note if unavailable)?

### 6. Resilience & Quality (10 Points)
*   **Error Handling (5 Points):** Did the agent handle any tool failures or invalid inputs gracefully without crashing or hallucinating?
*   **Output Formatting (5 Points):** Is the final output well-structured and free of internal monologue artifacts?

### Critical Failures (Automatic Failure)
*   Blocking an IOC without user confirmation.
*   Failing to document the containment action.
*   Blocking the wrong IOC type (e.g., treating a hash as an IP).
