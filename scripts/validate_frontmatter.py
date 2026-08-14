#!/usr/bin/env python3
"""Validate YAML frontmatter across rules_bank and skills content.

Hard failures (exit 1):
  - frontmatter missing or not parseable as YAML
  - skills/**/SKILL.md: missing name/description/type, or name != directory name
  - rules_bank/personas/*.md: missing name or description (required for
    Claude Code agent registration via the .claude/agents symlink)
  - rules_bank/run_books/**/*.md: missing title or type

Warnings (reported, exit 0):
  - missing generated block or generated.at timestamp

Usage: python3 scripts/validate_frontmatter.py [repo_root]
"""

import pathlib
import sys

import yaml

errors = []
warnings = []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        errors.append(f"{path}: frontmatter is not valid YAML ({exc})")
        return None
    return data if isinstance(data, dict) else None


def require(path, data, keys):
    for key in keys:
        if not data or key not in data or data[key] in (None, ""):
            errors.append(f"{path}: missing required frontmatter key '{key}'")


def check_generated(path, data):
    generated = (data or {}).get("generated")
    if not isinstance(generated, dict):
        warnings.append(f"{path}: no generated block")
    elif "at" not in generated:
        warnings.append(f"{path}: generated block missing 'at' timestamp")


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")

    for path in sorted(root.glob("skills/**/SKILL.md")):
        data = frontmatter(path)
        if data is None:
            errors.append(f"{path}: missing or unparseable frontmatter")
            continue
        require(path, data, ["name", "description", "type"])
        if data.get("name") and data["name"] != path.parent.name:
            errors.append(
                f"{path}: name '{data['name']}' != directory '{path.parent.name}'"
            )
        check_generated(path, data)

    for path in sorted(root.glob("rules_bank/personas/*.md")):
        data = frontmatter(path)
        if data is None:
            errors.append(f"{path}: missing or unparseable frontmatter")
            continue
        require(path, data, ["name", "description"])

    for path in sorted(root.glob("rules_bank/run_books/**/*.md")):
        data = frontmatter(path)
        if data is None:
            errors.append(f"{path}: missing or unparseable frontmatter")
            continue
        require(path, data, ["title", "type"])
        check_generated(path, data)

    for warning in warnings:
        print(f"WARN  {warning}")
    for error in errors:
        print(f"ERROR {error}")
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
