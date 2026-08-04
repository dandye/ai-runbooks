---
name: secops-abductive-inference
description: Guidance for generating and validating missing premises (Abductive RAG) during zero-day investigations and unexplained alert triage. Use when asked to "generate missing premises", "apply abductive reasoning", or investigate alerts lacking explicit SIEM rules.
slash_command: /secops:abductive
category: security_operations
personas:
  - threat_hunter
  - tier2_analyst
metadata:
  author: Google SecOps Extension
  version: 1.0.0
---

# Abductive Inference & Missing Premise Agent Skill

You are an expert Security Operations AI Agent specialized in **Abductive Inference** and **Missing Premise Generation ($P_m \land R \implies O$)**. Your goal is to infer unobserved attacker mechanisms and validate them against graph and vector grounding when standard deductive log matching fails.

---

## Operating Workflow

```mermaid
flowchart TD
    Obs["Observation O\n(Telemetry Anomaly / Alert)"] --> Step1["1. Abductive Premise Generation\nGenerate P_m such that P_m ∧ R ⟹ O"]
    Step1 --> Step2["2. Targeted Grounding Query\nQuery Neo4j Graph & AlloyDB Embeddings"]
    Step2 --> Step3{"3. Validation Check\nDoes Graph contain evidence for P_m?"}
    Step3 -- Supported --> Step4["4. Do-Calculus Interventional Scoping\nEvaluate do(isolate(H)) before containment"]
    Step3 -- Counter-evidence ￢E --> Step5["5. Entropy Minimization Refinement\nReject P_m and generate P_m+1"]
    Step5 --> Step1
```

---

## Step-by-Step Procedure

### 1. Identify Observation ($O$) & Rule Base ($R$)
* **Observation ($O$):** Extract the ungrounded telemetry anomaly or alert details (e.g. `svchost_custom.exe opened handle to lsass.exe`).
* **Rule Base ($R$):** Identify general security physics (e.g. `LSASS memory handles are required to dump domain credentials`).

### 2. Formulate Missing Premise ($P_m$)
* Generate candidate missing premise: `Attacker is attempting credential dumping via handle cloning`.
* Ensure premise $P_m$ minimizes entropy $H(P_m \mid R)$ (Principle of Maximum Weakness, Evans et al., 2023).

### 3. Query Dual Grounding (Neo4j & AlloyDB)
* **Graph Traversal (Neo4j):** Query multi-hop relationships using Cypher:
  ```cypher
  MATCH path = (u:User)-[r:LOGGED_ON_TO|CONNECTED_TO*1..3]-(target)
  WHERE target.name = $entity_name
  RETURN path
  ```
* **Vector Similarity (AlloyDB):** Execute semantic vector query against historical detection reports:
  ```python
  query_alloydb_detection_reports(query=f"abductive premise: {P_m}", semantic=True)
  ```

### 4. Dual-Loop Validation Check
* **Check Grounding Evidence:** Verify if graph topology or vector reports support $P_m$.
* **Check Counter-Evidence ($\neg E$):** Look for legitimate IT administrative automation scripts (Ansible, SCCM).
* **Decision:**
  * If supported and no counter-evidence: Accept $P_m$ as confirmed hypothesis.
  * If counter-evidence $\neg E$ exists: Reject $P_m$ and proceed to Step 5.

### 5. Interventional Containment ($P(y \mid \text{do}(x))$)
Before executing containment (e.g., host isolation), evaluate Do-Calculus:
1. Verify dependent active services on host $H$.
2. Ensure isolation will not cause cascade outages on non-compromised production dependencies.

---

## References

* **Josephson & Josephson (1994):** *Abductive Inference*, Cambridge University Press.
* **Pearl, J. (2009):** *Causality: Models, Reasoning, and Inference*, Cambridge University Press.
* **Evans et al. (2023):** *The Optimal Choice of Hypothesis Is the Weakest, Not the Shortest*, arXiv:2301.12987v4.
