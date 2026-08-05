---
title: "Common Step: Query Memories"
type: "common_step"
category: "institutional_memory"
status: "active"
tags:
  - memory_query
  - procedural_enhancement
  - adaptive_learning
---

# Common Step: Query Memories

## Purpose

To search for and retrieve relevant institutional memories that may enhance or modify the current procedural step. This common step integrates adaptive learning capabilities into existing runbooks without requiring structural changes.

## Inputs

- `${CURRENT_RUNBOOK}`: Path to the runbook currently being executed
- `${CURRENT_PERSONA}`: Path to the persona file for context
- `${CURRENT_STEP}`: Description of the current procedural step
- `${STEP_CONTEXT}`: Additional context about entities, tools, or scenarios involved
- `${CONFIDENCE_THRESHOLD}`: Minimum confidence level for memory application (default: 0.7)

## Tools

- `search_files`: Search memory files for relevant matches
- `read_file`: Read matched memory files for detailed analysis
- `list_files`: Browse memory directories if needed

## Process

### 1. Memory Search Strategy

Search for memories using multiple strategies to ensure comprehensive coverage:

**Primary Search**: Direct runbook and persona matching
```
search_files pattern="runbook: \"${CURRENT_RUNBOOK}\"" directory="institutional_memory/memories/"
search_files pattern="persona: \"${CURRENT_PERSONA}\"" directory="institutional_memory/memories/"
```

**Secondary Search**: Step and context matching
```
search_files pattern="${CURRENT_STEP}" directory="institutional_memory/memories/"
search_files pattern="${STEP_CONTEXT}" directory="institutional_memory/memories/"
```

**Tertiary Search**: Related patterns and adaptations
```
search_files directory="institutional_memory/patterns/" pattern="${STEP_CONTEXT}"
search_files directory="institutional_memory/adaptations/" pattern="${CURRENT_PERSONA}"
```

### 2. Memory Relevance Assessment

For each memory found, evaluate:

- **Exact Match**: Memory targets same runbook, persona, and step
- **Partial Match**: Memory applies to same runbook or persona but different step
- **Pattern Match**: Memory addresses similar context or scenario
- **Tool Match**: Memory involves same tools or procedures

### 3. Confidence Filtering

Filter memories based on confidence thresholds:

- **High Confidence (≥0.9)**: Auto-apply with notification
- **Medium Confidence (0.7-0.89)**: Recommend with explanation
- **Low Confidence (0.4-0.69)**: Suggest with analyst approval required
- **Very Low (<0.4)**: Skip unless explicitly requested

### 4. Memory Ranking

Rank applicable memories by:

1. **Relevance Score**: Exact > Partial > Pattern > Tool matches
2. **Confidence Level**: Higher confidence memories prioritized
3. **Recency**: More recently updated memories favored
4. **Success Rate**: Higher success rate memories preferred
5. **Validation Count**: More validated memories prioritized

## Outputs

### Memory Query Results

Return structured results containing:

```yaml
memory_query_results:
  total_memories_found: 3
  high_confidence_matches: 1
  medium_confidence_matches: 2
  recommended_memory: "memories/triage_alerts_tier1_internal_db.md"
  alternative_memories: 
    - "memories/triage_alerts_tier1_sensor_xyz.md"
    - "memories/general_enrichment_optimization.md"
  application_recommendation: "auto_apply"  # or "recommend" or "suggest"
```

### Memory Details

For recommended memory, provide:

- **Memory File Path**: Full path to the memory file
- **Confidence Score**: Current confidence level
- **Application Criteria**: When this memory should be used  
- **Derived Procedure**: The enhanced procedure from the memory
- **Success Metrics**: How to measure memory effectiveness
- **Validation History**: Recent application outcomes

### Application Guidance

Provide clear guidance for memory application:

- **Auto-Apply**: High confidence memories that should be used automatically
- **Recommend**: Medium confidence memories that should be suggested to analyst
- **Suggest**: Low confidence memories requiring explicit analyst approval
- **Review Required**: Memories that need analyst review before application

## Integration Pattern

This common step integrates into existing runbooks as follows:

```markdown
## Original Runbook Step N: Entity Enrichment

1. **Pre-Step Memory Check:**
   - Execute `common_steps/query_memories.md` with:
     - `CURRENT_RUNBOOK` = "run_books/triage_alerts.md"
     - `CURRENT_PERSONA` = "personas/soc_analyst_tier_1.md"
     - `CURRENT_STEP` = "Step N: Entity Enrichment"
     - `STEP_CONTEXT` = "IOC enrichment, entity lookup"

2. **Memory Application Decision:**
   - **If High Confidence Memory Found**: Apply derived procedure automatically
   - **If Medium Confidence Memory Found**: Present recommendation to analyst
   - **If Low Confidence Memory Found**: Request analyst approval
   - **If No Relevant Memory Found**: Continue with original procedure

3. **Original Procedure** (if no memory applied):
   - [Original step content unchanged]

4. **Memory Outcome Logging:**
   - Document which memory was applied (if any)
   - Record application success/failure for memory validation
```

## Error Handling

### No Memories Found
- Continue with original procedure
- Log search attempt for memory effectiveness tracking
- Consider flagging for potential memory creation if procedure issues arise

### Multiple High-Confidence Conflicts
- Apply most recent memory with highest success rate
- Flag conflict for resolution by memory management process
- Document conflict in application log

### Memory File Corruption
- Skip corrupted memory and log error
- Continue with next best memory or original procedure
- Flag memory file for repair/retirement

## Performance Considerations

### Search Optimization
- Index memory files by runbook and persona for faster lookup
- Cache recent memory query results for repeated steps
- Limit search depth to prevent performance impact

### Memory Loading
- Only read full memory content for top-ranked matches
- Use lazy loading for memory details until needed
- Implement timeout for memory file reads

## Completion Criteria

- Memory search completed across all relevant directories
- Found memories filtered and ranked by relevance and confidence
- Application recommendation generated based on confidence thresholds
- Memory details loaded for recommended memories
- Integration guidance provided for seamless runbook execution

## Expected Outputs

- **Memory Query Results**: Structured list of applicable memories with rankings
- **Application Recommendation**: Clear guidance on how to use found memories
- **Enhanced Procedure**: Modified procedure incorporating memory improvements (if applicable)
- **Logging Information**: Data needed for memory validation and effectiveness tracking