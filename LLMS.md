# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a security operations (SOC) runbook and persona system designed to guide LLM agents through standardized security workflows. The repository contains documentation, procedural guides, and configuration scripts for AI-assisted security operations.

## Repository Structure

- `rules_bank/` - Master source directory containing all documentation, personas, and runbooks
  - `personas/` - Security role definitions (SOC Analysts, Threat Hunters, Incident Responders, etc.)
  - `run_books/` - Step-by-step procedural guides for security tasks
    - `common_steps/` - Reusable procedure components
    - `irps/` - Incident Response Plans for major incidents
    - `guidelines/` - Best practices and documentation guides
- `.claude/` - Claude Code configuration directory
  - `rules_bank/` - Symlink to ../rules_bank (provides access to all content)
- `.clinerules/` - Cline configuration directory
  - `rules_bank/` - Symlink to ../rules_bank (provides access to all content)
- `.gemini/` - Gemini CLI configuration directory
  - `rules_bank/` - Symlink to ../rules_bank (provides access to all content)
- `reports/` - Generated security reports and examples

## AI Tool Integration

This repository supports three AI coding assistants through a unified symlink structure:

1. **Claude Code**: Reads from `.claude/rules_bank/`
2. **Cline**: Reads from `.clinerules/rules_bank/`
3. **Gemini CLI**: Reads from `.gemini/rules_bank/`

All three tools access the same content through symlinks to the master `rules_bank/` directory. This ensures consistency and eliminates the need for content duplication.

## Configuration Scripts

### Setting Active Persona
```bash
python set_persona_rules.py <persona_name>
# Example: python set_persona_rules.py tier1_soc_analyst
```
Currently supported personas: `tier1_soc_analyst`, `threat_hunter`

### Linking Common Steps
```bash
python symlink_common_steps.py
```
Run this after changing personas to ensure common steps remain accessible.

## Key Concepts

- **Runbooks**: Tactical, step-by-step procedures for specific security tasks (alert triage, IOC enrichment, etc.)
- **IRPs**: End-to-end incident response plans for major incidents following PICERL lifecycle
- **Personas**: Predefined security roles with specific responsibilities, skills, and tool access
- **Dynamic Configuration**: Uses symlinks in `.clinerules/` to activate specific contexts

## Working with the Codebase

1. The primary content lives in `rules_bank/` - edit source files there, not in the symlinked directories
2. The symlinks in `.claude/`, `.clinerules/`, and `.gemini/` automatically reflect changes made to `rules_bank/`
3. The project uses MCP (Model Context Protocol) tools for integration with Google Cloud security services
4. Runbook actions map to specific agent tools (see `rules_bank/agent_tool_mapping.md`)

## Code Style

When writing Python scripts:
- Follow Google Python Style Guide
- Use `pyink` for formatting
- Use `isort` for import sorting
- Line length: 88 characters
- Indentation: 2 or 4 spaces (be consistent within files)

## Important Notes

- This is primarily a documentation repository - there are no build, test, or lint commands
- The symlink system provides unified access across Claude Code, Cline, and Gemini CLI
- All edits should be made to files in `rules_bank/`, not through the symlinks in `.claude/`, `.clinerules/`, or `.gemini/`
- Changes to `rules_bank/` automatically propagate to all three AI tools
- The project integrates with Chronicle SIEM, SOAR, Google Threat Intelligence, and Security Command Center
