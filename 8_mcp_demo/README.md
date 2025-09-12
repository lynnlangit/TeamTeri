# MCP Greetings Demo

A simple Model Context Protocol (MCP) server that provides multilingual greeting functionality.

## Overview

This demo showcases a basic MCP server implementation that exposes greeting tools and resources, allowing Claude to greet users in different languages using CSV data.

## Features

- **greet_user**: Greet a user by name in a specific or random language
- **list_languages**: Get all available greeting languages  
- **get_greeting_for_language**: Get the greeting word for a specific language
- **greetings://data resource**: Access to complete greetings dataset

## Getting Started

### 1. Install Dependencies

```bash
pip install mcp>=1.2.0
```

### 2. Run the MCP Server

```bash
python mcp_server.py
```

### 3. Configure Claude Code

The MCP configuration has been created at `.mcp.json` in this directory. Claude Code should automatically detect it when you open this project folder.

Alternatively, you can manually add this to your Claude Code MCP settings:

```json
{
  "mcpServers": {
    "greetings": {
      "command": "python3.11",
      "args": ["/Users/lynnlangit/Documents/GitHub/TeamTeri/8_mcp_demo/mcp_server.py"],
      "cwd": "/Users/lynnlangit/Documents/GitHub/TeamTeri/8_mcp_demo"
    }
  }
}
```

### 4. Test the Tools

Once connected, you can use Claude to:
- "Greet me in Spanish" 
- "What languages are available for greetings?"
- "Give me a random greeting with my name"

## Files

- `mcp_server.py`: Main MCP server implementation
- `samples/greetings.csv`: Greeting data (language, greeting pairs)
- `greeting_app.py`: Original standalone Python script
- `test_greeting.py`: Test version of the script

## Requirements

- Python 3.10 or higher
- MCP Python SDK 1.2.0+