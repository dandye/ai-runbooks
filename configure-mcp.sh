#!/bin/bash

# Check if .mcp.json exists
if [ ! -f ".mcp.json" ]; then
    echo "Error: .mcp.json file not found in current directory"
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed"
    exit 1
fi

# Get all server names from the JSON file
server_names=$(jq -r '.mcpServers | keys[]' .mcp.json)

# Loop through each server and add it
for server_name in $server_names; do
    echo "Adding MCP server: $server_name"

    # Extract the server configuration and add it
    server_config=$(jq ".mcpServers[\"$server_name\"]" .mcp.json)

    if claude mcp add-json "$server_name" "$server_config"; then
        echo "✓ Successfully added $server_name"
    else
        echo "✗ Failed to add $server_name"
    fi

    echo ""
done

echo "Finished processing all MCP servers"