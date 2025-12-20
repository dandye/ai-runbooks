---
title: "Data Lake Queries (Placeholder)"
type: "runbook"
category: "security_operations"
status: "active"
tags:
  - data_lake
  - queries
  - historical_analysis
  - siem
---

# Runbook: Data Lake Queries

## Objective

To query the security data lake for specific historical data, large-scale analysis, trend identification, or information not readily available via standard SIEM searches. This runbook enables analysts to leverage BigQuery capabilities for deep historical analysis, bulk data processing, and complex analytical queries that exceed normal SIEM limitations in scope or timeframe.

## Scope

Focuses on constructing and executing BigQuery SQL queries against security datasets for historical analysis, bulk operations, and complex data correlation. Covers schema exploration, query optimization, result analysis, and proper data handling procedures. Includes data export capabilities and integration with SOAR documentation. Excludes real-time alerting, streaming analytics, or operational detection use cases - those are handled by SIEM-based runbooks.

## Inputs

*   `${QUERY_OBJECTIVE}`: Description of the data needed or the question to answer.
*   `${TARGET_DATASETS}`: Comma-separated list of BigQuery tables/datasets to query (e.g., `my_project.my_dataset.my_table`).
*   `${TIME_RANGE_START}`: Start timestamp for the query (e.g., ISO 8601 format).
*   `${TIME_RANGE_END}`: End timestamp for the query (e.g., ISO 8601 format).
*   *(Optional) `${SPECIFIC_FIELDS}`: Comma-separated list of specific fields to retrieve.*
*   *(Optional) `${FILTER_CONDITIONS}`: Specific WHERE clause conditions.*

## Tools

*   `bigquery`: `execute-query`, `describe-table`, `list-tables`
*   **Action:** Generate report file (e.g., using `write_to_file`)
*   `secops-soar`: `post_case_comment` (Optional, for documenting query/results)

## Workflow Steps & Diagram

1.  **Define Query:** Based on `${QUERY_OBJECTIVE}`, `${TARGET_DATASETS}`, time range, and filters, construct the BigQuery SQL query. Use `describe-table` or `list-tables` if needed to confirm schema/table names.
2.  **Execute Query:** Run the query using `bigquery.execute-query`.
3.  **Analyze Results:** Review the query results.
4.  **Format/Save Results (Optional):** If needed, format the results and save them to a file using the "Generate report file" action.
5.  **Document (Optional):** Document the query executed and a summary of the results in a relevant SOAR case using `post_case_comment`.
6.  **Completion:**
    *   **Action:** Generate a Mermaid sequence diagram summarizing the specific actions taken during this execution.
    *   **Action:** Record the current date and time of execution.
    *   **Action:** (Optional) Record the token usage and runtime duration if available from the environment.
    *   Conclude the runbook execution.

```mermaid
sequenceDiagram
    participant Analyst/User
    participant Cline as Cline (MCP Client)
    participant BigQuery as bigquery
    participant SOAR as secops-soar (Optional)

    Analyst/User->>Cline: Start Data Lake Query\nInput: QUERY_OBJECTIVE, TARGET_DATASETS, TIME_RANGE...

    %% Step 1: Define Query
    opt Need Schema/Table Info
        Cline->>BigQuery: list-tables() / describe-table(table_name=...)
        BigQuery-->>Cline: Table/Schema Info
    end
    Note over Cline: Construct BigQuery SQL Query

    %% Step 2: Execute Query
    Cline->>BigQuery: execute-query(query=SQL_QUERY)
    BigQuery-->>Cline: Query Results

    %% Step 3: Analyze Results
    Note over Cline: Analyze query results

    %% Step 4: Format/Save Results (Optional)
    opt Save Results
        Note over Cline: Format results (e.g., CSV, JSON)
        Cline->>Cline: Generate report file (path="./query_results...", content=FormattedResults)
        Note over Cline: Results saved locally
    end

    %% Step 5: Document (Optional)
    opt Document in SOAR
        Cline->>SOAR: post_case_comment(case_id=..., comment="Data Lake Query Executed: [...], Summary: [...]")
        SOAR-->>Cline: Comment Confirmation
    end

    Cline->>Analyst/User: Conclude runbook (result="Data lake query executed. Results analyzed/saved/documented as requested.")

```

## Completion Criteria

- Query objective clearly defined with specific data requirements identified
- Target datasets and tables verified for existence and appropriate permissions
- SQL query constructed with proper syntax, optimization, and time boundaries
- Schema validation completed to ensure correct field references and data types
- Query executed successfully within reasonable time and resource constraints
- Results analyzed for relevance, accuracy, and completeness
- Large result sets properly handled with pagination or export mechanisms
- Findings summarized with key insights and analytical conclusions
- Results formatted and saved in appropriate format (CSV, JSON, or report)
- Query methodology and results documented in SOAR case if applicable
- Data handling procedures followed for sensitive or classified information
- Query performance metrics captured for optimization recommendations

## Expected Outputs

- **Query Results**: Raw data returned from BigQuery execution
- **Data Analysis Summary**: Key insights and patterns identified from results
- **Exported Data Files**: Formatted result sets saved for further analysis or sharing
- **Query Documentation**: SQL queries used with execution context and parameters
- **Performance Metrics**: Query execution time, data processed, and resource usage
- **SOAR Documentation**: Case comments with query summary and key findings
- **Recommendations**: Suggestions for query optimization or additional analysis
- **Workflow Documentation**: Sequence diagram showing actual MCP tools and servers used during execution
- **Runbook Reference**: Clear identification of which runbook was executed to generate the report

## Rubric

### 1. Query Construction (25 Points)
*   **Syntax (15 Points):** Did the agent construct a valid BigQuery SQL statement?
*   **Optimization (10 Points):** Did the agent apply filters (time, fields) to optimize the query?

### 2. Execution & Handling (25 Points)
*   **Execution (15 Points):** Did the agent successfully run the query (`execute-query`)?
*   **Result Handling (10 Points):** Did the agent handle the results appropriately (e.g., saving large results to a file)?

### 3. Documentation (20 Points)
*   **Logging (20 Points):** Did the agent document the query and a summary of the findings in the case?

### 4. Visual Summary (10 Points)
*   **Sequence Diagram (10 Points):** Did the agent produce a valid Mermaid sequence diagram summarizing the actions taken during the execution?

### 5. Operational Metadata (10 Points)
*   **Date/Time (5 Points):** Did the agent record the date and time of the execution?
*   **Cost/Runtime (5 Points):** Did the agent attempt to record token usage and runtime duration (or note if unavailable)?

### 6. Resilience & Quality (10 Points)
*   **Error Handling (5 Points):** Did the agent handle any tool failures or invalid inputs gracefully without crashing or hallucinating?
*   **Output Formatting (5 Points):** Is the final output well-structured and free of internal monologue artifacts?

### Critical Failures (Automatic Failure)
*   Executing an unbounded query (no time limit) on a massive dataset.
*   Failing to save or display the query results.
*   Generating invalid SQL syntax without attempting correction.
