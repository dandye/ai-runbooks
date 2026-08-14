# Pull Request

## Summary

<!-- What does this change and why? Reference any related issues. -->

## Content Checklist

- [ ] Edited source files in `rules_bank/` or `skills/` (not through platform symlinks)
- [ ] Frontmatter follows the OKF v0.2 schema (`python3 scripts/validate_frontmatter.py .` passes)
- [ ] New runbooks include Objective, Scope, Inputs, Tools, Workflow Steps and Diagram, Completion Criteria, and Rubric sections (see `rules_bank/run_books/guidelines/runbook_guidelines.md`)
- [ ] All referenced files and tools actually exist in the repo (or in `rules_bank/agent_tool_mapping.md`)
- [ ] New skills are cross-referenced from the relevant persona manifests in `skills/_personas/`
