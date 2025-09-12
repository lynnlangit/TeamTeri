#!/usr/bin/env python3
"""
MCP Server for Multilingual Greetings
Provides tools and resources for greeting users in different languages
"""

import csv
import random
import os
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("greetings")

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

@mcp.tool()
def greet_user(name: str, language: str = "") -> str:
    """
    Greet a user in a specified language or random language.
    
    Args:
        name: The name of the user to greet
        language: Optional specific language for greeting (e.g., "Spanish", "French")
    
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

@mcp.tool()
def list_languages() -> List[str]:
    """
    List all available languages for greetings.
    
    Returns:
        A list of available language names
    """
    greetings = load_greetings()
    return [greeting['language'] for greeting in greetings]

@mcp.tool()
def get_greeting_for_language(language: str) -> str:
    """
    Get the greeting word for a specific language.
    
    Args:
        language: The language name (e.g., "Spanish", "French")
    
    Returns:
        The greeting word in that language, or error message if not found
    """
    greetings = load_greetings()
    
    for greeting_data in greetings:
        if greeting_data['language'].lower() == language.lower():
            return greeting_data['greeting']
    
    available_languages = [g['language'] for g in greetings]
    return f"Language '{language}' not found. Available: {', '.join(available_languages)}"

@mcp.resource("greetings://data")
def get_greetings_data() -> str:
    """
    Provides access to the complete greetings dataset.
    
    Returns:
        JSON representation of all available greetings
    """
    import json
    greetings = load_greetings()
    return json.dumps(greetings, indent=2)

if __name__ == "__main__":
    mcp.run()