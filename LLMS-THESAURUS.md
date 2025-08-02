---
generated: 2025-01-26T17:15:00Z
directory: .
file_count: 8
---

# Thesaurus for Main Project Directory

## Notation Guide
- **BT**: Broader Term (parent/category term)
- **NT**: Narrower Term (child/specific term)
- **RT**: Related Term (associated but not hierarchical)
- **SN**: Scope Note (clarification or usage guidance)

## Terms

**AI ASSISTANTS**
  USE FOR: artificial intelligence assistants, ai agents, llm agents, coding assistants
  BT: automation systems
  NT: claude code, cline, gemini cli
  RT: model context protocol, personas, runbooks
  SN: Refers to AI-powered tools that assist with security operations and coding tasks

**AI RUNBOOKS**
  USE FOR: artificial intelligence runbooks, ai security procedures, automated workflows
  BT: security documentation
  NT: runbooks, irps
  RT: soc procedures, personas, ai assistants
  SN: Structured documentation designed to guide AI agents through security workflows

**ALERT TRIAGE**
  USE FOR: alert investigation, initial assessment, event analysis
  BT: security operations
  NT: suspicious login triage, malware alert analysis
  RT: incident response, threat hunting, soc analysts
  SN: First-level analysis of security alerts to determine priority and next actions

**CHRONICLE SIEM**
  USE FOR: chronicle, google chronicle, siem platform
  BT: security platforms
  RT: soc operations, log analysis, security events
  SN: Google's Security Information and Event Management platform

**CLAUDE CODE**
  USE FOR: claude.ai/code, claude ai assistant
  BT: ai assistants
  RT: model context protocol, coding assistance
  SN: Anthropic's AI coding assistant tool

**CLINE**
  USE FOR: cline assistant, ai coding tool
  BT: ai assistants
  RT: claude code, gemini cli
  SN: AI-powered coding assistant tool

**CONFIGURATION SCRIPTS**
  USE FOR: setup scripts, automation scripts, python scripts
  BT: automation tools
  NT: set_persona_rules.py, symlink_common_steps.py
  RT: personas, symlinks, repository setup
  SN: Python scripts for configuring the AI runbooks system

**CTI RESEARCHER**
  USE FOR: cyber threat intelligence researcher, threat intelligence analyst
  BT: security roles
  RT: threat hunting, incident response, intelligence analysis
  SN: Security professional focused on cyber threat intelligence gathering and analysis

**DETECTION ENGINEER**
  USE FOR: security detection engineer, rule engineer
  BT: security roles
  RT: detection rules, yara-l, security monitoring
  SN: Security professional who creates and maintains detection logic and rules

**GEMINI CLI**
  USE FOR: gemini command line interface, google gemini
  BT: ai assistants
  RT: claude code, cline
  SN: Google's AI assistant command-line interface

**GOOGLE THREAT INTELLIGENCE**
  USE FOR: gti, threat intelligence platform, virustotal
  BT: security platforms
  RT: ioc enrichment, threat hunting, malware analysis
  SN: Google's threat intelligence and malware analysis platform

**INCIDENT RESPONDER**
  USE FOR: incident response specialist, ir analyst
  BT: security roles
  RT: incident response plans, picerl lifecycle, security incidents
  SN: Security professional who handles security incident response activities

**INCIDENT RESPONSE PLANS**
  USE FOR: irps, response procedures, incident plans
  BT: security procedures
  NT: malware incident response, phishing response, ransomware response
  RT: incident responder, picerl lifecycle, security incidents
  SN: Structured plans for responding to specific types of security incidents

**IOC ENRICHMENT**
  USE FOR: indicator enrichment, threat intelligence enrichment, ioc analysis
  BT: threat intelligence
  NT: file hash analysis, domain analysis, ip analysis
  RT: google threat intelligence, threat hunting, malware analysis
  SN: Process of gathering additional context and intelligence about indicators of compromise

**MCP TOOLS**
  USE FOR: model context protocol tools, mcp servers, integration tools
  BT: integration systems
  NT: chronicle_mcp, gti_mcp, soar_mcp, scc_mcp
  RT: ai assistants, security platforms, api integration
  SN: Tools that provide standardized integration between AI assistants and security platforms

**MODEL CONTEXT PROTOCOL**
  USE FOR: mcp, context protocol, ai integration protocol
  BT: integration protocols
  NT: mcp tools, mcp servers
  RT: ai assistants, security platforms
  SN: Protocol for enabling AI assistants to interact with external tools and services

**PERSONAS**
  USE FOR: security roles, role definitions, user profiles
  BT: security roles
  NT: tier1_soc_analyst, tier2_soc_analyst, threat_hunter, incident_responder, cti_researcher
  RT: security operations, runbooks, ai assistants
  SN: Predefined security roles with specific responsibilities, skills, and tool access

**PICERL LIFECYCLE**
  USE FOR: picerl, incident response lifecycle, ir methodology
  BT: security methodologies
  RT: incident response plans, incident responder
  SN: Preparation, Identification, Containment, Eradication, Recovery, Lessons Learned - standard incident response process

**REPORT GENERATION**
  USE FOR: security reporting, automated reports, report writing
  BT: security documentation
  NT: alert reports, investigation reports, hunt reports, executive reports
  RT: reporting templates, security operations
  SN: Automated creation of structured security reports following standardized templates

**REPOSITORY STRUCTURE**
  USE FOR: file organization, directory layout, project structure
  BT: project organization
  NT: rules_bank, reports directory, configuration directories
  RT: symlinks, ai tool integration
  SN: Organized layout of directories and files supporting multiple AI tools

**RULES_BANK**
  USE FOR: rules bank, master source directory, content repository
  BT: repository structure
  NT: personas directory, run_books directory, documentation files
  RT: symlinks, ai tool integration, source files
  SN: Master source directory containing all documentation, personas, and runbooks

**RUNBOOKS**
  USE FOR: security procedures, tactical guides, step-by-step procedures
  BT: security procedures
  NT: alert triage, ioc enrichment, threat hunting, incident response
  RT: personas, ai assistants, security operations
  SN: Tactical, step-by-step procedures for specific security tasks

**SECURITY COMMAND CENTER**
  USE FOR: scc, google security command center, cloud security
  BT: security platforms
  RT: vulnerability management, cloud security, compliance
  SN: Google Cloud's centralized security and risk management platform

**SECURITY OPERATIONS**
  USE FOR: soc operations, security ops, cybersecurity operations
  BT: cybersecurity
  NT: alert triage, incident response, threat hunting, vulnerability management
  RT: soc analysts, security platforms, runbooks
  SN: Day-to-day activities involved in monitoring, detecting, and responding to security threats

**SECURITY PLATFORMS**
  USE FOR: security tools, cybersecurity platforms, security systems
  BT: cybersecurity technology
  NT: chronicle siem, google threat intelligence, security command center, soar platforms
  RT: mcp tools, security operations, integration
  SN: Technological platforms and tools used for cybersecurity operations

**SECURITY ROLES**
  USE FOR: cybersecurity roles, security positions, security professionals
  BT: organizational roles
  NT: soc analyst, threat hunter, incident responder, cti researcher, detection engineer
  RT: personas, security operations, responsibilities
  SN: Professional roles within cybersecurity and security operations teams

**SOAR PLATFORMS**
  USE FOR: soar, security orchestration automation response, security automation
  BT: security platforms
  RT: incident response, security operations, automation
  SN: Platforms that enable security orchestration, automation, and response capabilities

**SOC ANALYSTS**
  USE FOR: security operations center analysts, security analysts
  BT: security roles
  NT: tier1_soc_analyst, tier2_soc_analyst, tier3_soc_analyst
  RT: alert triage, security monitoring, incident detection
  SN: Security professionals who monitor and analyze security events in a Security Operations Center

**SUPERCLAUDE FRAMEWORK**
  USE FOR: superclaude, command framework, security commands
  BT: automation frameworks
  NT: security commands, slash commands, orchestrator
  RT: ai assistants, command execution, security workflows
  SN: Framework for executing security workflows through command-based interfaces

**SYMLINKS**
  USE FOR: symbolic links, file links, directory links
  BT: file system features
  RT: repository structure, ai tool integration, configuration
  SN: File system links that enable multiple AI tools to access the same content from different directories

**THREAT HUNTER**
  USE FOR: threat hunting specialist, proactive hunter, security hunter
  BT: security roles
  RT: threat hunting, proactive security, advanced persistent threats
  SN: Security professional who proactively searches for threats and indicators of compromise

**THREAT HUNTING**
  USE FOR: proactive hunting, threat detection, advanced threat detection
  BT: security operations
  RT: threat hunter, indicators of compromise, advanced persistent threats
  SN: Proactive searching for threats and indicators of compromise within an environment

**TIER1_SOC_ANALYST**
  USE FOR: tier 1 analyst, t1 analyst, junior soc analyst, level 1 analyst
  BT: soc analysts
  RT: alert triage, initial investigation, escalation
  SN: Entry-level SOC analyst responsible for initial alert triage and basic investigations

**TIER2_SOC_ANALYST**
  USE FOR: tier 2 analyst, t2 analyst, senior soc analyst, level 2 analyst
  BT: soc analysts
  RT: detailed investigation, escalation handling, complex analysis
  SN: Mid-level SOC analyst handling more complex investigations and escalated alerts

**TIER3_SOC_ANALYST**
  USE FOR: tier 3 analyst, t3 analyst, expert soc analyst, level 3 analyst
  BT: soc analysts
  RT: advanced investigation, threat hunting, complex incidents
  SN: Senior SOC analyst handling advanced investigations and complex security incidents