---
# REQUIRED FIELDS - All fields below are mandatory
runbook: "run_books/[runbook_name].md"                    # Source runbook file path
persona: "personas/[persona_name].md"                     # Applicable persona file path
source_step: "[Step X: Description]"                      # Specific runbook step modified
confidence: 0.0                                           # Confidence score (0.0-1.0, start at 0.0)
last_updated: "YYYY-MM-DD"                               # ISO date format
feedback_source: "[analyst_identifier]"                   # Source of original feedback
validation_count: 0                                       # Number of successful applications
success_rate: 0.0                                        # Ratio of successful/total applications
related_cases: []                                         # Array of related case IDs
memory_type: "[type]"                                    # See types below

# OPTIONAL FIELDS - Include if applicable
tags: []                                                  # Additional categorization tags
prerequisites: []                                         # Required conditions for memory application
expiration_date: "YYYY-MM-DD"                           # When memory should be reviewed/retired
priority: "normal"                                        # high, normal, low
applies_to_sensors: []                                   # Specific sensor/tool applicability
organizational_context: ""                               # Specific organizational factors
---

# Memory Title: [Descriptive title of the procedural modification]

## Analyst Feedback

*[Direct quote or paraphrase of the original analyst feedback that led to this memory]*

"Example: For our organization, when triaging alerts from the 'XYZ' sensor, we must always perform a historical lookup in our internal 'ThreatDB' before proceeding with public enrichment. This is a critical step that is currently missing."

## Context Analysis

**Original Procedure Issue**: *[Description of what was missing or suboptimal in the original runbook]*

**Organizational Context**: *[Specific organizational factors that necessitate this modification]*

**Risk Impact**: *[What risks are mitigated by implementing this memory]*

**Frequency**: *[How often this scenario occurs - helps prioritize memory application]*

## Original Procedure (for context)

*[Relevant excerpt from the original runbook step being modified]*

- **Tool**: `[original_tool_name]`
- **Parameters**: `[original_parameters]`
- **Expected Output**: *[what the original step produces]*

## Derived Procedure

*[New or modified procedure based on the institutional learning]*

1. **[Step 1 Name]**:
   - **Tool**: `[tool_name]`
   - **Parameters**: `[parameters]`
   - **Validation**: *[how to verify this step succeeded]*
   - **Fallback**: *[what to do if this step fails]*

2. **[Step 2 Name]** (if applicable):
   - **Condition**: *[when this step applies]*
   - **Tool**: `[tool_name]`
   - **Parameters**: `[parameters]`

## Application Criteria

*[Specific conditions under which this memory should be applied]*

- **Alert Types**: *[which alert types benefit from this memory]*
- **Sensor Sources**: *[specific sensors/tools this applies to]*
- **Threat Categories**: *[threat types where this is relevant]*
- **Time Constraints**: *[any timing considerations]*

## Validation Metrics

*[How to measure the effectiveness of this memory]*

- **Success Indicators**: *[what indicates successful application]*
- **Performance Metrics**: *[measurable improvements expected]*
- **Quality Metrics**: *[how this improves analysis quality]*

## Application Log

*[Chronological record of when and how this memory has been applied]*

- **YYYY-MM-DD**: Memory created based on feedback from [source]
- **YYYY-MM-DD**: Successfully applied to Case/Alert #[ID] - [brief outcome]
- **YYYY-MM-DD**: Applied to Case/Alert #[ID] - [outcome, adjust confidence if needed]

---

## Memory Types Reference

Use one of these standardized memory types:

- **procedure_modification**: Changes to existing runbook steps
- **procedure_addition**: New steps added to existing runbooks  
- **context_enhancement**: Additional context or validation steps
- **tool_substitution**: Alternative tools for specific scenarios
- **escalation_criteria**: Modified escalation triggers or thresholds
- **false_positive_pattern**: Known benign patterns to recognize
- **organizational_preference**: Org-specific operational preferences
- **compliance_requirement**: Regulatory or policy-driven modifications
- **performance_optimization**: Efficiency improvements to procedures
- **quality_enhancement**: Improvements to analysis depth or accuracy

## Confidence Scoring Guidelines

- **0.0-0.3**: Experimental/unvalidated memories (requires analyst approval)
- **0.4-0.6**: Low confidence (suggest with caution, track closely)
- **0.7-0.8**: Medium confidence (recommend with explanation)
- **0.9-1.0**: High confidence (apply automatically with notification)

## Validation Requirements

Memories must meet these criteria before confidence can increase above 0.3:

1. Applied successfully in at least 2 similar scenarios
2. No negative feedback from analysts
3. Measurable improvement in efficiency or quality
4. No unintended side effects observed
5. Documented approval from senior analyst or supervisor