#!/usr/bin/env python3
"""
Simple MCP-style Server for Multilingual Greetings (Python 3.9 compatible)
This is a basic JSON-RPC server that demonstrates MCP concepts without requiring the full SDK.
"""

import json
import sys
import csv
import random
import os
from typing import List, Dict, Any

def load_greetings() -> List[Dict[str, str]]:
    """Load greetings from the CSV file."""
    greetings = []
    csv_path = os.path.join('samples', 'greetings.csv')
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                greetings.append({
                    'language': row['language'],
                    'greeting': row['greeting']
                })
    except FileNotFoundError:
        # Fallback data if CSV file is not found
        greetings = [
            {'language': 'English', 'greeting': 'Hello'},
            {'language': 'Spanish', 'greeting': 'Hola'},
            {'language': 'French', 'greeting': 'Bonjour'}
        ]
    
    return greetings

def greet_user(name: str, language: str = "") -> str:
    """
    Greet a user in a specified language or random language.
    
    Args:
        name: The name of the user to greet
        language: Optional specific language for greeting
    
    Returns:
        A greeting message in the format "<Greeting> <Name>."
    """
    greetings = load_greetings()
    
    if language:
        # Find specific language greeting
        for greeting_data in greetings:
            if greeting_data['language'].lower() == language.lower():
                return f"{greeting_data['greeting']} {name}."
        
        # If language not found, return error message
        available_languages = [g['language'] for g in greetings]
        return f"Language '{language}' not available. Available languages: {', '.join(available_languages)}"
    
    # Random greeting if no language specified
    greeting_data = random.choice(greetings)
    return f"{greeting_data['greeting']} {name}."

def list_languages() -> List[str]:
    """List all available languages for greetings."""
    greetings = load_greetings()
    return [greeting['language'] for greeting in greetings]

def get_greeting_for_language(language: str) -> str:
    """Get the greeting word for a specific language."""
    greetings = load_greetings()
    
    for greeting_data in greetings:
        if greeting_data['language'].lower() == language.lower():
            return greeting_data['greeting']
    
    available_languages = [g['language'] for g in greetings]
    return f"Language '{language}' not found. Available: {', '.join(available_languages)}"

def handle_tools_list() -> Dict[str, Any]:
    """Return the list of available tools."""
    return {
        "tools": [
            {
                "name": "greet_user",
                "description": "Greet a user in a specified language or random language",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "The name of the user to greet"},
                        "language": {"type": "string", "description": "Optional specific language for greeting"}
                    },
                    "required": ["name"]
                }
            },
            {
                "name": "list_languages", 
                "description": "List all available languages for greetings",
                "inputSchema": {"type": "object", "properties": {}}
            },
            {
                "name": "get_greeting_for_language",
                "description": "Get the greeting word for a specific language", 
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "language": {"type": "string", "description": "The language name"}
                    },
                    "required": ["language"]
                }
            }
        ]
    }

def handle_tool_call(name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Handle a tool call request."""
    try:
        if name == "greet_user":
            result = greet_user(arguments.get("name", ""), arguments.get("language", ""))
            return {"content": [{"type": "text", "text": result}]}
        elif name == "list_languages":
            result = list_languages()
            return {"content": [{"type": "text", "text": f"Available languages: {', '.join(result)}"}]}
        elif name == "get_greeting_for_language":
            result = get_greeting_for_language(arguments.get("language", ""))
            return {"content": [{"type": "text", "text": result}]}
        else:
            return {"error": f"Unknown tool: {name}"}
    except Exception as e:
        return {"error": f"Tool execution failed: {str(e)}"}

def main():
    """Simple demo of the MCP-style server functionality."""
    print("=== MCP Greetings Demo Server ===")
    print("This demonstrates the tools that would be available in a real MCP server.\n")
    
    # Demo the tools
    print("Available tools:")
    tools = handle_tools_list()
    for tool in tools["tools"]:
        print(f"- {tool['name']}: {tool['description']}")
    
    print("\n--- Demo tool calls ---")
    
    # Demo greet_user
    result = handle_tool_call("greet_user", {"name": "Alice", "language": "Spanish"})
    print(f"greet_user(Alice, Spanish): {result['content'][0]['text']}")
    
    # Demo list_languages  
    result = handle_tool_call("list_languages", {})
    print(f"list_languages(): {result['content'][0]['text']}")
    
    # Demo get_greeting_for_language
    result = handle_tool_call("get_greeting_for_language", {"language": "French"})
    print(f"get_greeting_for_language(French): {result['content'][0]['text']}")
    
    print("\nTo use with real MCP:")
    print("1. Upgrade to Python 3.10+")
    print("2. pip install mcp")
    print("3. Use mcp_server.py with the MCP SDK")

if __name__ == "__main__":
    main()