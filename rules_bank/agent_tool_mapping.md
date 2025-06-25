# Agent Tool Mapping

This document maps the conceptual, agent-agnostic actions used in the runbooks to the specific tool implementations available to the Cline agent. This serves as a reference for understanding how procedural steps are executed and can be used as a guide for adapting the runbooks to other automation agents.

| Conceptual Action | Cline Agent Tool | Description |
| :--- | :--- | :--- |
| **Generate report file** | `write_to_file` | Creates a new file or overwrites an existing one with specified content. Used for generating reports. |
| **Request user input** | `ask_followup_question` | Prompts the user for information or confirmation before proceeding with an action. |
| **Conclude runbook** | `attempt_completion` | Signals the end of a runbook's execution and presents the final summary or result. |
| **Execute local command** | `execute_command` | Runs a command-line interface (CLI) command on the local system. |
| **Read file contents** | `read_file` | Reads and returns the full content of a specified file. |
| **Search file contents** | `search_files` | Performs a regular expression search across files in a directory. |
| **List directory contents** | `list_files` | Lists the files and subdirectories within a specified directory. |
| **Make targeted file edits** | `replace_in_file` | Performs a search-and-replace operation on specific parts of a file. |
| **Use MCP Tool** | `use_mcp_tool` | Executes a tool provided by a connected Model Context Protocol (MCP) server. |
| **Access MCP Resource** | `access_mcp_resource` | Accesses a data resource provided by a connected MCP server. |
