---
title: "Common Step: Apply Memory Procedure"
type: "common_step"
category: "institutional_memory"
status: "active"
tags:
  - memory_application
  - procedural_enhancement
  - adaptive_execution
---

# Common Step: Apply Memory Procedure

## Purpose

To safely apply institutional memory-derived procedures while maintaining proper validation, logging, and fallback capabilities. This common step ensures consistent memory application across all runbooks with appropriate safeguards.

## Inputs

- `${MEMORY_FILE}`: Path to the memory file containing the derived procedure
- `${ORIGINAL_PROCEDURE}`: The original runbook procedure being enhanced/replaced
- `${APPLICATION_CONTEXT}`: Current operational context (case ID, alert details, etc.)
- `${ANALYST_APPROVAL}`: Whether analyst has approved memory application (for low-confidence memories)
- `${FALLBACK_REQUIRED}`: Whether fallback to original procedure should be available

## Tools

- `read_file`: Read memory file for procedure details
- `use_mcp_tool`: Execute memory-specified tools and procedures
- `ask_followup_question`: Get analyst approval when required
- `replace_in_file`: Update memory application log

## Process

### 1. Memory Validation

Before applying memory, validate:

**Memory File Integrity**:
- Confirm memory file exists and is readable
- Verify YAML frontmatter is properly formatted
- Check that derived procedure section is complete

**Application Criteria Check**:
- Verify current context matches memory application criteria
- Confirm persona alignment with memory requirements
- Validate that prerequisites are met

**Confidence Assessment**:
- Check if confidence level meets execution threshold
- Determine if analyst approval is required
- Assess any recent performance indicators

### 2. Analyst Interaction (if required)

For memories requiring approval (confidence < 0.7):

```
ask_followup_question: "Institutional memory suggests an enhanced procedure for this step. 

Original Procedure: ${ORIGINAL_PROCEDURE}

Enhanced Procedure (from memory): ${DERIVED_PROCEDURE}

Memory Details:
- Confidence: ${CONFIDENCE_SCORE}
- Success Rate: ${SUCCESS_RATE}  
- Last Updated: ${LAST_UPDATED}
- Source: ${FEEDBACK_SOURCE}

Would you like to:
1. Apply the enhanced procedure
2. Use the original procedure
3. Apply with modifications (please specify)

Your choice:"
```

### 3. Procedure Execution

Execute the memory-derived procedure with proper monitoring:

**Pre-Execution Setup**:
- Log application attempt with timestamp
- Set up fallback triggers and conditions
- Prepare validation metrics collection

**Step-by-Step Execution**:
- Execute each step in the derived procedure
- Monitor for errors or unexpected outcomes
- Validate intermediate results against success criteria
- Collect performance metrics (time, accuracy, completeness)

**Error Handling**:
- If any step fails, evaluate fallback conditions
- Log failure details for memory validation
- Either retry with modifications or fall back to original procedure

### 4. Outcome Validation

Assess the results of memory application:

**Success Indicators**:
- All procedure steps completed successfully
- Results meet or exceed original procedure expectations
- No unintended side effects observed
- Performance metrics show improvement

**Quality Assessment**:
- Compare output quality to original procedure baseline
- Verify completeness of analysis or investigation
- Check for any information gaps or errors

**Performance Measurement**:
- Time efficiency compared to original procedure
- Resource utilization (tool calls, API requests, etc.)
- Analyst satisfaction with process and results

### 5. Application Logging

Update memory file with application results:

```yaml
# Add to memory file application_log section
- date: "2025-08-23T14:30:00Z"
  context: "${APPLICATION_CONTEXT}"
  outcome: "success"  # success, partial_success, failure
  performance_metrics:
    time_saved_seconds: 120
    quality_improvement: "high"
    analyst_satisfaction: 4.5
  notes: "Procedure applied successfully, reduced enrichment time by 2 minutes"
```

## Decision Matrix

### Memory Application Decision Tree

```
IF confidence >= 0.9:
  → Apply automatically with notification
  → Log application for validation
  
ELIF confidence >= 0.7:
  → Present recommendation to analyst
  → Apply if approved, otherwise use original
  
ELIF confidence >= 0.4:
  → Request explicit analyst approval
  → Explain memory rationale and risks
  
ELSE:
  → Skip memory application
  → Continue with original procedure
  → Log skip reason for analysis
```

### Fallback Conditions

Trigger fallback to original procedure if:
- Memory procedure fails at any step
- Results don't meet minimum quality thresholds
- Analyst explicitly requests fallback
- Tool dependencies are not available
- Context changes during execution make memory inappropriate

## Integration Examples

### High-Confidence Automatic Application

```markdown
## Enhanced Step: IOC Enrichment with Internal Database Check

**Memory Applied**: `memories/triage_alerts_tier1_internal_db.md` (Confidence: 0.95)

1. **Internal Database Lookup**:
   - Tool: `internal_db query`
   - Parameters: `database=ThreatDB, query=${IOC_VALUE}`
   - Expected: Internal threat history and context

2. **Conditional External Enrichment**:
   - Condition: If internal lookup returns no results OR confidence < 0.8
   - Tool: `secops-mcp enrich_ioc`
   - Parameters: `ioc=${IOC_VALUE}`

**Original Procedure Available**: [Details logged for comparison]
**Performance Tracking**: Enabled for validation
```

### Medium-Confidence Recommended Application

```markdown
## Step Enhancement Available

**Memory Recommendation**: `memories/hunt_optimization_timeframe.md` (Confidence: 0.75)

The system suggests an optimized timeframe selection for this hunt based on previous successful hunts with similar TTPs. 

**Recommended Enhancement**: 
- Start with 7-day lookback instead of 30-day default
- Focus on business hours (9 AM - 5 PM) for initial sweep
- Expand timeframe only if initial results are promising

**Would you like to apply this enhancement?** [Y/n]
```

## Error Recovery

### Graceful Degradation

If memory application fails:

1. **Log Failure**: Record detailed error information
2. **Assess Impact**: Determine if partial completion is acceptable
3. **Fallback Decision**: Auto-fallback or request analyst decision
4. **Continue Execution**: Resume with original or modified procedure

### Memory Quality Feedback

Failed applications provide valuable feedback:

- Update memory confidence score based on failure type
- Flag memory for review if failures indicate systematic issues
- Consider memory refinement or retirement if appropriate

## Completion Criteria

- Memory application decision made based on confidence and context
- If applied, all memory procedure steps executed successfully
- Outcome properly validated against success criteria
- Application results logged for memory validation
- Any fallback or error conditions handled appropriately
- Performance metrics collected for effectiveness assessment

## Expected Outputs

- **Enhanced Results**: Improved procedure outcomes from memory application
- **Application Log**: Detailed record of memory usage for validation
- **Performance Metrics**: Quantified improvements or issues
- **Fallback Status**: Information about any fallback actions taken
- **Quality Assessment**: Comparison with original procedure baseline

## Quality Assurance

Before completing memory application:

- [ ] Memory validation completed successfully
- [ ] Application criteria verified and met
- [ ] Analyst approval obtained if required
- [ ] All procedure steps executed or fallback completed
- [ ] Results validated against success criteria
- [ ] Application logged with detailed outcome information
- [ ] Performance metrics collected and recorded
- [ ] Any errors or issues properly handled and documented