# server.py
import os
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Add a file reading tool
@mcp.tool()
def read_file(file_path: str) -> str:
    """Read the contents of a file"""
    if not os.path.exists(file_path):
        return "File not found"
    with open(file_path, 'r') as file:
        return file.read()

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"