---
type: "Playbook"
title: "Neo4j Graph Relationship Traversal and Blast Radius Analysis"
description: "Procedure for querying Neo4j knowledge graphs to calculate lateral movement scope, Active Directory privilege escalation paths, and compromised entity blast radius."
resource: "ai-runbooks/rules_bank/run_books/neo4j_graph_traversal_and_blast_radius.md"
timestamp: "2026-08-04T17:42:56Z"
provenance:
  source_type: "manual"
  source_tool: "Antigravity"
  timestamp: "2026-08-04T17:42:56Z"
---

# Neo4j Graph Relationship Traversal & Blast Radius Analysis

## Objective

Guide SOC analysts and Threat Hunter agents in leveraging Neo4j multi-hop graph relationship traversals to quantify incident blast radius, trace Active Directory privilege escalation paths, and accelerate secondary asset containment.

## Scope

This runbook applies to incident investigations involving compromised hosts, service accounts, or user identities where graph topology data is available via `query_knowledge_graph`.

## Inputs

*   `${INITIAL_ENTITY_ID}`: Initial compromised hostname or user account (e.g., `FINANCE-SRV-01`, `svc_finance`, `dev_admin`, `WRK-DEV-04`).
*   `${TRAVERSAL_TYPE}`: Focus of traversal (`lateral_movement` or `privilege_escalation`).
*   `${MAX_HOPS}`: Traversal depth constraint (default: 1 to 3 hops).

## Tools Used

*   `neo4j-mcp`: `query_knowledge_graph` (Cypher relationship traversal).
*   `secops-mcp`: `search_security_events`, `search_udm` (SIEM fallback telemetry).
*   `secops-soar`: `save_report_artifact`, `execute_manual_action` (containment).

## Cypher Schema Exemplars

### 1. Host Connectivity & Lateral Movement Traversal
When investigating host compromise or service account abuse across adjacent network assets:
```cypher
MATCH path = (u:User {name: $entity_name})-[r:LOGGED_ON_TO|CONNECTED_TO*1..3]-(target)
RETURN path, target.name AS asset_name, labels(target) AS asset_type;
```

### 2. Active Directory Privilege Escalation Path Traversal
When investigating high-privilege account compromise (`Domain Admins`, `dev_admin`) or domain pivoting:
```cypher
MATCH path = (u:User {name: $entity_name})-[r:MEMBER_OF|HAS_ADMIN|CAN_REACH*1..3]-(target)
RETURN path, target.name AS asset_name, labels(target) AS asset_type;
```

---

## Workflow Steps

### Step 1: Initial Entity Identification & Cypher Formulation
1. Extract primary compromised entity identifiers (`User.name` or `Host.name`) from the initial alert.
2. Select Cypher relationship patterns based on investigation type:
   * **Lateral Movement:** Traverses `LOGGED_ON_TO` and `CONNECTED_TO` relationships.
   * **Privilege Escalation:** Traverses `MEMBER_OF` (Group membership), `HAS_ADMIN`, and `CAN_REACH` relationships.

### Step 2: Multi-Hop Graph Traversal (`query_knowledge_graph`)
1. Execute `query_knowledge_graph` with parameterized Cypher queries.
2. If Cypher query returns nodes:
   * Compile list of all reachable hosts (`Host`), users (`User`), domain groups (`Group`), and database servers (`Host {type: "database_server"}`).
   * Flag high-value targets (e.g., `Domain Admins`, `PROD-DB-01`).
3. If Cypher query returns no records:
   * Proceed immediately to **Step 3 (SIEM Fallback Procedure)**.

### Step 3: Telemetry Fallback Procedure (SIEM Log Querying)
When graph query returns zero matching records (indicating data gap or un-indexed host):
1. Fall back to Chronicle SIEM UDM queries (`search_security_events` / `search_udm`).
2. Query UDM logs for network connections (`NETWORK_CONNECTION`), authentication events (`USER_LOGIN`), and DNS requests (`NETWORK_DNS`) originating from `${INITIAL_ENTITY_ID}` within lookback window.
3. Document graph data gap in investigation notes.

### Step 4: Blast Radius Calculation & Isolation Action Plan
1. Consolidate identified blast radius entities into priority tiers:
   * **Tier 1 (Immediate Isolation):** Directly compromised host and secondary hosts connected via active service account sessions or admin privileges.
   * **Tier 2 (Credential Revocation):** Compromised user accounts and member service accounts requiring immediate password resets and session termination.
   * **Tier 3 (Perimeter Block):** Malicious external C2 domains and IP addresses.
2. Formulate containment recommendations for Tier 2 Incident Responder.
3. Save structured investigation report using `save_report_artifact`.
