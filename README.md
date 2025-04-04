# try-mcp

This project is a demonstration of the Model Context Protocol (MCP) using the Python SDK. MCP is designed to facilitate the integration and management of machine learning models in various environments.

From <https://github.com/modelcontextprotocol/python-sdk>

## Installation

To install the necessary dependencies, run:
`uv sync`

## Running the Server

### With MCP Inspector

To start the MCP development server, use the following command:
`uv run mcp dev server.py`

Navigate to: `http://localhost:5173/`

### With Claude Desktop

install the mcp server

`uv run mcp install server.py`

Note - needs to point to the proper local `uv` location:

```json
{
  "mcpServers": {
    "Demo": {
      "command": "/Users/mjm/.asdf/shims/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/mjm/projects/try-mcp/server.py"
      ]
    }
  }
}
```