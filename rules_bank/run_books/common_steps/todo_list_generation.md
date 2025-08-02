# Todo List Generation for Security Operations

## Overview
This guide provides structured approaches for LLMs to create and manage todo lists for complex security operations tasks. Effective todo list generation is critical for maintaining organization, tracking progress, and ensuring comprehensive task completion in security workflows.

## When to Use Todo Lists

<reasoning>
Todo lists should be created when:
- A task involves multiple discrete steps or components
- The work spans multiple tools or platforms (SIEM, SOAR, threat intelligence)
- There are dependencies between tasks that need careful sequencing
- The investigation or response may take extended time
- Multiple team members or systems need visibility into progress
- Complex incident response requiring PICERL lifecycle management
</reasoning>

## Markdown Checkbox Syntax for State Tracking

<reasoning>
Markdown checkboxes provide visual and programmatic state tracking that LLMs can easily parse and update. The checkbox syntax (`- [ ]` for pending, `- [x]` for completed) offers several advantages:
1. Clear visual representation of progress
2. Easy pattern matching for LLMs to identify completed vs pending tasks
3. Native markdown support in most tools and platforms
4. Simple to update by replacing `[ ]` with `[x]`
5. Maintains readability for both humans and AI
</reasoning>

### Checkbox State Patterns

- `- [ ]` - Task is pending/not started
- `- [x]` - Task is completed
- `- [~]` - Task is cancelled/skipped (strikethrough: ~~task~~)
- `- [>]` - Task is in progress (custom notation)
- `- [!]` - Task is blocked (custom notation)

<example>
Basic Todo List with Checkboxes:
- [x] Review initial alert details
- [x] Identify affected systems
- [>] Collect network logs from past 24 hours
- [ ] Analyze logs for suspicious patterns
- [!] Get approval for containment actions (waiting on management)
- [ ] Execute containment plan
- [~] ~~Schedule vendor meeting~~ (no longer needed)
</example>

### Threshold Guidelines
- **Simple Tasks (< 3 steps)**: May not require formal todo tracking
- **Moderate Tasks (3-10 steps)**: Should use todo lists for organization
- **Complex Tasks (> 10 steps)**: Must use todo lists with priority levels

## Task Decomposition Strategies

<reasoning>
Effective task decomposition requires:
1. Understanding the overall objective
2. Identifying discrete, actionable components
3. Recognizing dependencies and sequencing requirements
4. Assigning appropriate priority levels
5. Estimating complexity for each subtask
</reasoning>

### Decomposition Patterns

#### Pattern 1: Top-Down Hierarchical
Break complex tasks into major phases, then subdivide each phase.

<example>
User Request: "Investigate and respond to a potential data exfiltration incident"

Generated Todo List:
## Initial Assessment Phase
- [ ] Review alert details and context
- [ ] Identify affected systems and users
- [ ] Determine incident severity and scope

## Evidence Collection Phase
- [ ] Collect network logs from affected timeframe
- [ ] Gather endpoint telemetry data
- [ ] Export relevant SIEM events

## Analysis Phase
- [ ] Analyze network traffic patterns
- [ ] Review user behavior analytics
- [ ] Correlate with threat intelligence

## Containment Phase
- [ ] Isolate affected systems
- [ ] Disable compromised accounts
- [ ] Block malicious IPs/domains

## Documentation Phase
- [ ] Create incident timeline
- [ ] Document findings and IoCs
- [ ] Generate executive summary
</example>

#### Pattern 2: Tool-Based Organization
Organize tasks by the security tools or platforms required.

<example>
User Request: "Perform threat hunt for PowerShell abuse"

Generated Todo List:
## Chronicle SIEM Tasks
- [ ] Search for PowerShell execution events
- [ ] Filter for encoded commands
- [ ] Identify unusual parent processes

## SOAR Platform Tasks
- [ ] Create hunting case
- [ ] Document suspicious findings
- [ ] Assign to appropriate team

## Threat Intelligence Tasks
- [ ] Check command patterns against known TTPs
- [ ] Search for related IoCs
- [ ] Correlate with threat actor profiles

## Endpoint Analysis Tasks
- [ ] Review PowerShell logs on suspicious hosts
- [ ] Check for persistence mechanisms
- [ ] Analyze command history
</example>

#### Pattern 3: Timeline-Based Sequencing
Structure tasks based on temporal dependencies and urgency.

<reasoning>
Timeline-based organization helps when:
- Certain tasks must complete before others can begin
- There are time-sensitive elements (SLA, containment windows)
- Evidence may degrade or rotate out over time
- Coordination with other teams is required
</reasoning>

<example>
User Request: "Respond to ransomware alert"

Generated Todo List:
IMMEDIATE (0-15 minutes):
- Verify ransomware alert validity
- Identify affected systems
- Initiate containment procedures
- Alert incident response team

SHORT-TERM (15-60 minutes):
- Isolate infected endpoints
- Capture memory dumps
- Preserve evidence
- Check backup integrity

MEDIUM-TERM (1-4 hours):
- Analyze ransomware variant
- Search for additional infections
- Review attack timeline
- Coordinate with stakeholders

LONG-TERM (4+ hours):
- Plan recovery strategy
- Document lessons learned
- Update detection rules
- Conduct post-incident review
</example>

## Priority Assignment Logic

<reasoning>
Priority levels should reflect:
- Business impact of the task
- Dependencies (blocking other tasks)
- Time sensitivity
- Resource requirements
- Regulatory or compliance needs
</reasoning>

### Priority Framework
- **CRITICAL**: Immediate action required, blocks all other work
- **HIGH**: Important for investigation/response success
- **MEDIUM**: Should be completed but not immediately urgent
- **LOW**: Nice to have, can be deferred if needed

<example>
Ransomware Response Priority Assignment:

CRITICAL:
- Isolate infected systems
- Preserve volatile evidence
- Stop encryption spread

HIGH:
- Identify patient zero
- Determine attack vector
- Check backup viability

MEDIUM:
- Update threat intelligence
- Document timeline
- Notify stakeholders

LOW:
- Update runbooks
- Schedule lessons learned
- Archive evidence long-term
</example>

## Complex Investigation Todo Lists with Checkboxes

### Multi-Stage APT Investigation

<example>
User Request: "Investigate suspected APT activity across our cloud infrastructure"

Generated Todo List:

## PHASE 1: INITIAL SCOPING
- [x] Review initial indicators and alerts (COMPLETED - 3 suspicious IAM events found)
- [x] Identify potentially affected cloud projects (COMPLETED - proj-123, proj-456 affected)
- [>] Establish investigation timeline (IN PROGRESS - correlating timestamps)
- [ ] Create dedicated SOAR case

PHASE 2: CLOUD INFRASTRUCTURE ANALYSIS
5. Audit IAM permissions changes (CRITICAL)
6. Review cloud audit logs for anomalies (CRITICAL)
7. Check for unauthorized API usage (HIGH)
8. Analyze resource creation/deletion patterns (HIGH)
9. Review network flow logs (MEDIUM)

PHASE 3: THREAT INTELLIGENCE CORRELATION
10. Search for known APT IoCs (HIGH)
11. Analyze TTPs against MITRE ATT&CK (HIGH)
12. Query threat intelligence for similar campaigns (MEDIUM)
13. Check for infrastructure overlap with known groups (MEDIUM)

PHASE 4: LATERAL MOVEMENT INVESTIGATION
14. Trace authentication flows between services (CRITICAL)
15. Identify service account abuse (CRITICAL)
16. Map potential pivot points (HIGH)
17. Review cross-project access patterns (HIGH)

PHASE 5: EVIDENCE PRESERVATION
18. Export relevant logs before retention expires (CRITICAL)
19. Capture cloud resource configurations (HIGH)
20. Document network topologies (MEDIUM)
21. Create evidence chain of custody (MEDIUM)

PHASE 6: CONTAINMENT PLANNING
22. Identify containment options without alerting attacker (CRITICAL)
23. Plan credential rotation strategy (CRITICAL)
24. Prepare network segmentation changes (HIGH)
25. Draft communication plan (MEDIUM)

PHASE 7: RESPONSE EXECUTION
26. Execute containment measures (CRITICAL)
27. Monitor for attacker response (CRITICAL)
28. Validate containment effectiveness (HIGH)
29. Begin recovery procedures (HIGH)

PHASE 8: POST-INCIDENT ACTIVITIES
30. Complete incident report (HIGH)
31. Update detection rules (HIGH)
32. Conduct lessons learned session (MEDIUM)
33. Share threat intelligence (MEDIUM)
34. Update incident response procedures (LOW)
</example>

## Task Status Management with Checkboxes

<reasoning>
Proper status management ensures:
- Clear visibility into progress
- No tasks are forgotten or duplicated
- Team coordination is maintained
- Audit trail for compliance
- Accurate time tracking for metrics
- LLMs can pattern match checkbox states to understand current progress
</reasoning>

### Checkbox State Transitions

<example>
Progressive Status Updates During Investigation:

**Initial State:**
```markdown
## Investigation Tasks
- [ ] Search for lateral movement indicators
- [ ] Review authentication logs
- [ ] Check for privilege escalation
- [ ] Document findings in SOAR case
```

**After Starting First Task:**
```markdown
## Investigation Tasks
- [>] Search for lateral movement indicators (IN PROGRESS - analyzing past 24h)
- [ ] Review authentication logs
- [ ] Check for privilege escalation
- [ ] Document findings in SOAR case
```

**After Completing First Task:**
```markdown
## Investigation Tasks
- [x] Search for lateral movement indicators (COMPLETED - found 3 suspicious events)
- [>] Review authentication logs (IN PROGRESS)
- [ ] Check for privilege escalation
- [ ] Document findings in SOAR case
```

**When Blocked:**
```markdown
## Investigation Tasks
- [x] Search for lateral movement indicators (COMPLETED - found 3 suspicious events)
- [!] Review authentication logs (BLOCKED - waiting for log access from IT team)
- [ ] Check for privilege escalation
- [ ] Document findings in SOAR case
```

**Final State:**
```markdown
## Investigation Tasks
- [x] Search for lateral movement indicators (COMPLETED - found 3 suspicious events)
- [x] Review authentication logs (COMPLETED - analyzed 2 compromised accounts)
- [x] Check for privilege escalation (COMPLETED - detected UAC bypass)
- [x] Document findings in SOAR case (COMPLETED - case #3506 updated)
```
</example>

### LLM Pattern Matching for Progress Tracking

<reasoning>
LLMs can efficiently track progress by:
1. Counting `[x]` vs `[ ]` to calculate completion percentage
2. Identifying `[!]` items that need attention or escalation
3. Focusing on `[>]` items as current work in progress
4. Recognizing patterns like all subtasks complete = parent task ready
</reasoning>

<example>
Progress Calculation:
```markdown
## Incident Response (7/10 tasks = 70% complete)
- [x] Initial triage
- [x] Evidence collection
- [x] Malware analysis
- [>] Containment actions (3/5 systems isolated)
- [!] Legal notification (awaiting legal team input)
- [ ] Recovery planning
- [x] Network isolation
- [x] Account suspension
- [x] IoC documentation
- [ ] Post-incident review
```
</example>

## Best Practices for LLM Todo Generation

### 1. Granularity Balance
<reasoning>
Tasks should be specific enough to be actionable but not so granular that the list becomes unwieldy. Each todo item should represent a meaningful unit of work that can be completed in a reasonable timeframe.
</reasoning>

**Too Granular:**
- Open Chronicle
- Click on search
- Type query
- Press enter

**Appropriate Granularity:**
- Search Chronicle for authentication anomalies in past 24 hours

### 2. Clear Success Criteria
Each todo should have implicit or explicit completion criteria.

<example>
GOOD: "Identify all systems that communicated with malicious IP 192.168.1.100"
- Clear target (malicious IP)
- Specific scope (all systems)
- Measurable outcome (list of systems)

POOR: "Look into network stuff"
- Vague objective
- No scope definition
- Unclear completion state
</example>

### 3. Dependency Notation
When tasks have dependencies, note them clearly.

<example>
Todo List with Dependencies:
1. Export firewall logs for past week (PRIORITY: HIGH)
2. [DEPENDS ON #1] Analyze firewall logs for C2 communications
3. [DEPENDS ON #2] Create block list for identified C2 servers
4. [DEPENDS ON #3] Deploy updated firewall rules
</example>

### 4. Time Estimates
For complex operations, include time estimates to aid planning.

<example>
Incident Response Todo with Time Estimates:
1. Initial triage and validation [15-30 min]
2. Forensic evidence collection [2-3 hours]
3. Malware analysis [1-2 hours]
4. Impact assessment [30-45 min]
5. Remediation planning [1 hour]
6. Execution and validation [2-4 hours]
7. Report generation [1-2 hours]

Total Estimated Time: 7.5-13.25 hours
</example>

## Integration with Security Workflows

### SOAR Case Management Integration
<reasoning>
Todo lists should align with SOAR case structures and workflows. This ensures consistency between task tracking and case management systems.
</reasoning>

<example>
SOAR-Aligned Todo Structure:
1. Case Setup
   - Create SOAR case with appropriate classification
   - Link related alerts and observables
   - Assign to appropriate team/analyst

2. Investigation Tasks
   - Execute detection playbook
   - Gather enrichment data
   - Perform entity analysis

3. Response Actions
   - Execute containment playbook
   - Validate response effectiveness
   - Update case status

4. Documentation
   - Add investigation notes to case
   - Attach evidence and artifacts
   - Generate case report
</example>

### Compliance and Audit Considerations
<reasoning>
In regulated environments, todo lists serve as audit trails. They should capture:
- Who performed each task
- When tasks were completed
- What evidence supports completion
- Any deviations from standard procedures
</reasoning>

## Displaying Todo Lists for User Visibility

<reasoning>
LLMs should proactively display todo lists to users at key points:
1. After initial task decomposition - shows the planned approach
2. At regular intervals during long investigations - provides progress updates
3. When blocked or needing user input - clarifies what's pending
4. At task completion - demonstrates what was accomplished
5. When context switching between major phases - maintains awareness
</reasoning>

### When to Display Todo Lists

<example>
User: "Investigate the suspicious PowerShell activity on WINS-D19"

LLM Response:
I'll investigate the suspicious PowerShell activity on WINS-D19. Let me create a comprehensive investigation plan:

## Investigation Todo List:
- [ ] Query Chronicle SIEM for PowerShell events from WINS-D19
- [ ] Filter for encoded/obfuscated commands
- [ ] Check for unusual parent processes
- [ ] Correlate with authentication events
- [ ] Search for related network connections
- [ ] Check GTI for known malicious patterns
- [ ] Document findings in SOAR case
- [ ] Generate investigation report

Starting with the SIEM query now...

[After completing some tasks, show progress:]

## Progress Update (5/8 tasks completed):
- [x] Query Chronicle SIEM for PowerShell events from WINS-D19 ✓
- [x] Filter for encoded/obfuscated commands ✓ (found 3 suspicious commands)
- [x] Check for unusual parent processes ✓ (detected cmd.exe → powershell chain)
- [x] Correlate with authentication events ✓ (linked to user compromise)
- [x] Search for related network connections ✓ (identified C2 communication)
- [ ] Check GTI for known malicious patterns
- [ ] Document findings in SOAR case
- [ ] Generate investigation report

Found critical indicators of compromise. Continuing with threat intelligence correlation...
</example>

### Progress Display Patterns

<reasoning>
Different scenarios require different display approaches:
- Simple tasks: Show initial list, then completion summary
- Complex tasks: Show initial list, periodic progress updates, final summary
- Blocked tasks: Highlight what's blocking and what's still pending
- Failed tasks: Show what succeeded before failure
</reasoning>

<example>
## Blocked Task Display:
Current Status - 3/7 tasks completed, 1 blocked:
- [x] Initial triage completed
- [x] Evidence collected from endpoint
- [x] Memory dump captured
- [!] Malware analysis (BLOCKED - sandbox environment offline)
- [ ] Create IoC list
- [ ] Update detection rules
- [ ] Write incident report

⚠️ Waiting for sandbox environment to come back online to continue malware analysis.
</example>

## Including Todo Lists in Security Reports

<reasoning>
Todo lists serve multiple purposes in security reports:
1. Executive Summary - High-level task completion metrics
2. Methodology Section - Shows systematic approach taken
3. Timeline Documentation - Demonstrates when tasks were completed
4. Appendix - Detailed task breakdown for audit purposes
5. Lessons Learned - Identifies which tasks took longest or were blocked
</reasoning>

### Report Integration Examples

<example>
# Security Investigation Report - Case #3506

## Executive Summary
Investigation Status: 85% Complete (17/20 tasks completed)
- Critical tasks: 100% complete
- High priority: 90% complete  
- Medium priority: 60% complete

## Investigation Methodology
The investigation followed a structured approach with the following phases:

### Phase 1: Initial Assessment ✓
- [x] Alert validation
- [x] Scope identification
- [x] Severity classification

### Phase 2: Evidence Collection ✓
- [x] Network log extraction
- [x] Endpoint telemetry gathering
- [x] Memory forensics

### Phase 3: Analysis (In Progress)
- [x] Malware behavioral analysis
- [x] C2 infrastructure mapping
- [>] Attribution analysis (75% complete)
- [ ] Full kill chain reconstruction

## Detailed Findings
[Report continues with findings linked to specific completed tasks...]

## Appendix A: Complete Task Tracking
[Full todo list with timestamps and status updates]
</example>

### Automated Report Todo Sections

<reasoning>
LLMs should automatically include relevant todo information in reports:
1. Completion percentage in executive summary
2. Task timeline in methodology
3. Blocked items in challenges/limitations section
4. Incomplete tasks in recommendations/next steps
</reasoning>

<example>
## Report Template with Integrated Todo Tracking:

```markdown
# Incident Response Report - [Incident Name]
Generated: [Date/Time]

## Response Status Overview
**Overall Progress:** X/Y tasks (Z%) completed

### Critical Tasks:
- [x] Containment actions (100% complete)
- [x] Evidence preservation (100% complete)

### Investigation Tasks:
- [x] Root cause analysis (complete)
- [>] Full environment sweep (in progress)
- [ ] Threat actor attribution (pending)

### Recovery Tasks:
- [ ] System restoration (planned)
- [ ] Monitoring enhancement (planned)

## Investigation Timeline
Based on task completion records:
- T+0:15 - Initial response tasks completed
- T+1:00 - Containment achieved
- T+3:00 - Evidence collection finalized
- T+6:00 - Analysis phase 80% complete

[Rest of report...]
```
</example>

## Common Pitfalls to Avoid

1. **Over-Planning**: Don't spend more time planning than executing
2. **Under-Specifying**: Vague todos lead to incomplete work
3. **Ignoring Dependencies**: Can cause workflow blockages
4. **Static Lists**: Todo lists should evolve as investigation progresses
5. **Missing Context**: Each todo should be understandable in isolation
6. **Not Displaying Progress**: Users need visibility into ongoing work
7. **Omitting from Reports**: Todo lists provide valuable audit trails

<reasoning>
As investigations progress, new information may require todo list updates. LLMs should be prepared to:
- Add new tasks as discoveries are made
- Reprioritize based on findings
- Remove tasks that become irrelevant
- Split complex tasks that prove larger than expected
</reasoning>

<example>
Adaptive Todo Evolution:

Initial List:
1. Investigate suspicious login from unusual location

After Initial Analysis:
1. ~~Investigate suspicious login from unusual location~~ (COMPLETED)
2. NEW: Check for MFA bypass attempts (CRITICAL) 
3. NEW: Review all logins from identified malicious IP (HIGH)
4. NEW: Audit user's recent permission changes (HIGH)
5. NEW: Check for data access anomalies post-login (MEDIUM)
</example>

## Conclusion

Effective todo list generation is essential for managing complex security operations. By following these patterns and practices, LLMs can create organized, actionable task lists that improve investigation efficiency and ensure comprehensive coverage of security incidents.

Remember: The goal is not just to create lists, but to facilitate effective action and maintain clear progress visibility throughout security operations.