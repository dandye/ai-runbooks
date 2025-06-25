# AI Runbooks for Security Operations

This repository contains a comprehensive security operations (SOC) runbook and persona system designed to guide LLM agents through standardized security workflows.

## Overview

The project provides structured documentation, procedural guides, and configuration scripts that enable AI assistants (Claude Code, Cline, and Gemini CLI) to effectively assist with security operations tasks.

## Repository Structure

```
dandye_ai_runbooks/
├── rules_bank/                    # Master source directory for all content
│   ├── personas/                  # Security role definitions
│   ├── run_books/                 # Procedural guides for security tasks
│   │   ├── common_steps/         # Reusable procedure components
│   │   ├── irps/                 # Incident Response Plans
│   │   └── guidelines/           # Best practices and documentation
│   └── [other documentation]     # Configuration and reference files
├── .claude/                      # Claude Code configuration directory
│   └── rules_bank/               # Symlink to ../rules_bank
├── .clinerules/                  # Cline configuration directory
│   └── rules_bank/               # Symlink to ../rules_bank
├── .gemini/                      # Gemini CLI configuration directory
│   └── rules_bank/               # Symlink to ../rules_bank
├── reports/                      # Generated security reports
├── set_persona_rules.py          # Script to configure active personas
└── symlink_common_steps.py       # Script to manage common steps symlinks
```

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
- Compatible with the same documentation structure

## Symlink Architecture

The project uses a symlink-based system to share the same content across all three AI tools:

1. **Master Content**: All documentation, personas, and runbooks are maintained in `rules_bank/`
2. **Symlinks**: Each AI tool's configuration directory contains a symlink to `rules_bank/`
3. **Benefits**: 
   - Single source of truth for all content
   - Updates automatically propagate to all AI tools
   - No duplication or synchronization needed

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

## Usage

1. **For AI Assistants**: The symlinked `rules_bank` directory in each tool's configuration folder provides access to all personas, runbooks, and documentation.

2. **For Developers**: 
   - Edit content only in the `rules_bank/` directory
   - Never edit files through the symlinks
   - Use the provided Python scripts for persona configuration if needed

3. **For Security Teams**: Use this repository to standardize and document your security operations procedures for AI-assisted workflows.

## Configuration Scripts

- `set_persona_rules.py`: Configure active personas (legacy - may need updates for new structure)
- `symlink_common_steps.py`: Manage common steps symlinks (legacy - may need updates)

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