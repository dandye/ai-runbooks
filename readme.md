# AI Runbooks for Security Operations

This repository provides security operations runbooks and role-based guides for AI-assisted cybersecurity workflows.

## Overview

Built by and for enterprise security teams, this project standardizes incident  response procedures and threat analysis workflows across multiple AI platforms including Claude, Gemini, and Cline. It equips LLMs with specialized context and cognitive tools to perform complex security investigations with the same rigor and consistency as experienced analysts.

## Key Components

### Personas
Security role definitions including:
- SOC Analysts (Tier 1-3)
- Threat Hunters
- Incident Responders
- CTI Researchers
- Security Engineers
- And more...

### Runbooks
Step-by-step procedural guides for:
- Alert triage
- IOC enrichment and investigation
- Threat hunting
- Incident response
- Case management
- And many more security operations tasks

### Incident Response Plans (IRPs)
Comprehensive end-to-end strategies for:
- Malware incidents
- Phishing attacks
- Ransomware
- Compromised accounts

## Repository Structure

```
ai_runbooks/
├── rules_bank/                    # Master source directory for all content
│   ├── personas/                  # Security role definitions
│   ├── run_books/                 # Procedural guides for security tasks
│   │   ├── common_steps/         # Reusable procedure components
│   │   ├── irps/                 # Incident Response Plans
│   │   └── guidelines/           # Best practices and documentation
│   └── [other documentation]     # Configuration and reference files
├── reports/                      # Generated security reports
├── mcp-security/                 # MCP server implementations
└── [configuration files]         # Various setup and config scripts
```

## Usage

1. **For Security Teams**: Use this repository to standardize and document your security operations procedures for AI-assisted workflows.

2. **For Developers**:
   - Edit content only in the `rules_bank/` directory
   - Never edit files through the symlinks in AI tool directories
   - Use the provided Python scripts for configuration if needed

3. **For AI Assistants**: The symlinked `rules_bank` directory in each tool's configuration folder provides access to all personas, runbooks, and documentation.

## Integration

This project is designed to work with:
- Chronicle SIEM
- SOAR platforms
- Google Threat Intelligence (GTI)
- Security Command Center (SCC)
- Various MCP (Model Context Protocol) tools

## Contributing

See `CONTRIBUTING` file for guidelines on contributing to this project.

## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.

---

## AI Tool Integration

This repository is designed to work with three AI coding assistants:

### Claude Code (claude.ai/code)
- Uses the `.claude/` directory for configuration
- Reads context from `.claude/rules_bank/` symlink
- See `CLAUDE.md` for Claude-specific guidance

### Cline
- Uses the `.clinerules/` directory for configuration
- Reads context from `.clinerules/rules_bank/` symlink
- Follows the same runbook and persona system

### Gemini CLI
- Uses the `.gemini/` directory for configuration
- Reads context from `.gemini/rules_bank/` symlink
- See `GEMINI.md` for Gemini-specific guidance
- Compatible with the same documentation structure

### Quick Start for AI Tools

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd dandye_ai_runbooks
   ```

2. The symlinks should already be set up. Verify they exist:
   ```bash
   ls -la .claude/rules_bank
   ls -la .clinerules/rules_bank
   ls -la .gemini/rules_bank
   ```

3. If symlinks are missing, create them manually:
   ```bash
   # For Claude Code
   mkdir -p .claude
   ln -s ../rules_bank .claude/rules_bank

   # For Cline
   mkdir -p .clinerules
   ln -s ../rules_bank .clinerules/rules_bank

   # For Gemini CLI
   mkdir -p .gemini
   ln -s ../rules_bank .gemini/rules_bank
   ```

### Using with AI Tools

Each AI tool will automatically read the context from its respective directory:
- **Claude Code**: Reads from `.claude/`
- **Cline**: Reads from `.clinerules/`
- **Gemini CLI**: Reads from `.gemini/`

All three tools access the same content through symlinks, ensuring consistency.

### Symlink Architecture

The project uses a symlink-based system to share the same content across all three AI tools:

1. **Master Content**: All documentation, personas, and runbooks are maintained in `rules_bank/`
2. **Symlinks**: Each AI tool's configuration directory contains a symlink to `rules_bank/`
3. **Benefits**:
   - Single source of truth for all content
   - Updates automatically propagate to all AI tools
   - No duplication or synchronization needed

### Configuration Scripts

- `set_persona_rules.py`: Configure active personas (legacy - may need updates for new structure)
- `symlink_common_steps.py`: Manage common steps symlinks (legacy - may need updates)
- `configure_mcp_tools.py`: Configure MCP (Model Context Protocol) tools for Claude Desktop

## Example Runbook Invocation Prompts

Use these realistic prompts to invoke various security runbooks. All examples use real data extracted from the `reports/` directory:

### Alert Triage
```
Please execute the alert triage runbook for SOAR case 2194.
```
The case involves repeated authentication failures for user F.K. on host A.S.L from IP 10.1.0.4. Check for duplicate cases and perform initial entity enrichment.

### IOC Enrichment
```
Run the basic IOC enrichment runbook for the suspicious domain scarfponcho.com.
```
Threat intelligence analysis and SIEM correlation for a domain which was flagged in our environment.

```
Execute IOC enrichment for the file hash de96a6e69944335375dc1ac238336066889d9ffc7d73628ef4fe1b1b160ab32c found on host WINS-D19.
```
This was associated with PowerShell obfuscation activity by user LISAWALKER.

### Case Investigation
```
Perform a comprehensive case investigation for SOAR case 3480.
```
 This is a critical priority case involving PowerShell attacks on WINS-D19, potential data exfiltration via BigQuery, and GCP exploitation attempts. Focus on the 17 associated alerts.

### Detection Rule Analysis
```
Analyze detection rule ru_99d1f620-3fe2-41d5-918e-0e1bd2402065 (ursnif_malware_dns).
```
 I need rule validation, tuning recommendations, and analysis of recent detections for this high-severity rule.

### Threat Hunting
```
Execute the IOC threat hunt runbook for IP addresses 46.8.9.205, 46.8.9.206, and 46.8.9.207.
```
These IPs are associated with the malicious domain scarfponcho.com and need comprehensive SIEM analysis.

```
Run the advanced threat hunting runbook focusing on lateral movement techniques (PSExec, WMI) around host WINS-D19.
```
This follows the PowerShell attack activity discovered in case 3480.

### Malware Triage
```
Perform malware triage for the sample with hash de96a6e69944335375dc1ac238336066889d9ffc7d73628ef4fe1b1b160ab32c.
```
This was involved in the PowerShell obfuscation incident on WINS-D19.

### Suspicious Login Analysis
```
Execute the suspicious login triage runbook for authentication events involving user F.K. on host A.S.L from source IP 10.1.0.4.
```
This is related to case 2194 with multiple failed followed by successful logins.

### Incident Response
```
Initiate incident response for compromised user account in case 3480.
```
Multiple indicators suggest account compromise including PowerShell obfuscation and potential data exfiltration.

### Cloud Security Analysis
```
Run the cloud vulnerability triage runbook for the BigQuery exfiltration alerts in case 3480.
```
Focus on the DLP context and Google Drive data movement patterns detected by SCC.

### Endpoint Isolation
```
Execute the basic endpoint triage and isolation runbook for host WINS-D19.
```
This system was compromised in case 3480 with PowerShell attacks and potential malware execution.

### Deep Dive Analysis
```
Perform a deep dive IOC analysis on domain scarfponcho.com using GTI collections.
```
Include malware family associations, campaign attribution, and infrastructure analysis.

### Summary
These examples demonstrate how to invoke runbooks with specific, actionable intelligence that mirrors real security operations scenarios.