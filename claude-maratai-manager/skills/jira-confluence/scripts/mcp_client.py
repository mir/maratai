#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "httpx>=0.27",
#   "pyyaml>=6.0",
# ]
# requires-python = ">=3.12"
# ///
"""
Python MCP client for Atlassian MCP server.

Implements MCP protocol over Streamable HTTP transport (POST /v1/mcp).
Session ID is obtained from the Mcp-Session-Id response header during
initialization and included in all subsequent requests.

Usage:
    # List available tools
    python mcp_client.py list-tools

    # Call a specific tool
    python mcp_client.py call <tool_name> '{"arg": "value"}'
"""

import argparse
import json
import sys
from typing import Any

import httpx
import yaml

# Import token functions from oauth module
from oauth import get_valid_token, AuthenticationError

# Import shared utilities
from common import yaml_output

# Import configuration
from config import MCP_URL, MCP_PROTOCOL_VERSION


class MCPError(Exception):
    """Base exception for MCP errors."""

    pass


class ProtocolError(MCPError):
    """MCP protocol error."""

    pass


class AtlassianMCPClient:
    """
    Python client for Atlassian MCP server.

    Implements MCP protocol over Streamable HTTP transport.
    All requests are POSTed to MCP_URL. Session ID is obtained from
    the Mcp-Session-Id response header during initialization.
    """

    def __init__(self, token: str | None = None):
        if token:
            self.token = token
        else:
            try:
                self.token = get_valid_token()
            except AuthenticationError as e:
                raise AuthenticationError(
                    f"No token found: {e}. Run 'auth.py login' first."
                )

        self.session_id: str | None = None
        self.request_id = 0
        self._initialized = False

    def _next_id(self) -> int:
        """Get next request ID."""
        self.request_id += 1
        return self.request_id

    def _get_headers(self) -> dict[str, str]:
        """Get HTTP headers for MCP requests."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {self.token}",
        }
        if self.session_id:
            headers["Mcp-Session-Id"] = self.session_id
        return headers

    def _post(self, payload: dict, timeout: float = 30.0) -> dict:
        """Send POST to MCP_URL and return parsed JSON-RPC result."""
        with httpx.Client(timeout=timeout) as client:
            response = client.post(MCP_URL, json=payload, headers=self._get_headers())

        # Capture session ID from response header
        if "Mcp-Session-Id" in response.headers:
            self.session_id = response.headers["Mcp-Session-Id"]

        if response.status_code == 401:
            raise AuthenticationError(
                "Authentication failed. Run 'auth.py login' to refresh token."
            )

        if response.status_code not in (200, 202):
            raise ProtocolError(f"HTTP {response.status_code}: {response.text}")

        content_type = response.headers.get("Content-Type", "")

        if "text/event-stream" in content_type:
            return self._parse_sse_response(response.text, payload["id"])

        if "application/json" in content_type:
            result = response.json()
            if "error" in result:
                raise ProtocolError(f"JSON-RPC error: {result['error']}")
            return result.get("result", {})

        raise ProtocolError(f"Unexpected content type: {content_type}")

    def _parse_sse_response(self, text: str, request_id: int) -> dict:
        """Parse inline SSE response body to extract JSON-RPC result."""
        result = None
        for line in text.split("\n"):
            line = line.strip()
            if line.startswith("data:"):
                data = line[5:].strip()
                if data:
                    try:
                        parsed = json.loads(data)
                        if parsed.get("id") == request_id:
                            if "result" in parsed:
                                result = parsed["result"]
                            elif "error" in parsed:
                                raise ProtocolError(
                                    f"JSON-RPC error: {parsed['error']}"
                                )
                    except json.JSONDecodeError:
                        continue

        if result is None:
            raise ProtocolError("No valid response in SSE stream")

        return result

    def connect(self) -> str | None:
        """Initialize MCP session. Returns session ID."""
        self.initialize()
        return self.session_id

    def initialize(self) -> dict:
        """
        Send MCP initialize request and capture session ID from response header.

        Returns:
            Server capabilities
        """
        params = {
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {},
            "clientInfo": {
                "name": "atlassian-skill-python",
                "version": "1.0.0",
            },
        }
        req_id = self._next_id()
        payload = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": "initialize",
            "params": params,
        }
        result = self._post(payload, timeout=10.0)
        self._initialized = True

        # Send initialized notification
        try:
            notif = {"jsonrpc": "2.0", "method": "notifications/initialized"}
            with httpx.Client(timeout=5.0) as client:
                client.post(MCP_URL, json=notif, headers=self._get_headers())
        except Exception:
            pass  # Notification may not be required

        return result

    def _send_request_impl(
        self,
        method: str,
        params: dict | None = None,
        request_id: int | None = None,
        timeout: float = 30.0,
    ) -> dict:
        """Send JSON-RPC request to MCP server."""
        if not self._initialized:
            self.initialize()

        if request_id is None:
            request_id = self._next_id()
        payload = {"jsonrpc": "2.0", "id": request_id, "method": method}
        if params:
            payload["params"] = params

        return self._post(payload, timeout=timeout)

    def _send_request_with_retry(self, method: str, params: dict | None = None) -> dict:
        """
        Send request with automatic retry on timeout.

        First attempt: 2 second timeout (fast fail for connection issues)
        On timeout: Check auth, reinitialize, retry with 20 second timeout
        """
        try:
            return self._send_request_impl(method, params, timeout=2.0)
        except ProtocolError as e:
            if "Timeout" not in str(e):
                raise  # Re-raise non-timeout errors

            print("Connection timeout, reconnecting...", file=sys.stderr)

            try:
                self.token = get_valid_token()
            except AuthenticationError:
                raise AuthenticationError(
                    "Authentication expired during retry. Run 'auth.py login'"
                )

            self.session_id = None
            self._initialized = False
            self.initialize()

            try:
                return self._send_request_impl(method, params, timeout=20.0)
            except ProtocolError as retry_error:
                if "Timeout" in str(retry_error):
                    raise ProtocolError(
                        f"Request timed out after retry. "
                        f"The Atlassian MCP server may be slow or unavailable. "
                        f"Method: {method}"
                    )
                raise

    def _send_request(self, method: str, params: dict | None = None) -> dict:
        """Send request with automatic retry on timeout."""
        return self._send_request_with_retry(method, params)

    def close(self):
        """No-op: Streamable HTTP has no persistent connection to close."""
        pass

    def list_tools(self) -> list[dict]:
        """List available tools on the MCP server."""
        if not self._initialized:
            self.initialize()
        result = self._send_request("tools/list")
        return result.get("tools", [])

    def call_tool(
        self, name: str, arguments: dict | None = None, return_full_result: bool = False
    ) -> Any:
        """
        Call a tool on the MCP server.

        Args:
            name: Tool name
            arguments: Tool arguments
            return_full_result: If True, return full MCP result including metadata

        Returns:
            Tool result content (or full result dict if return_full_result=True)
        """
        if not self._initialized:
            self.initialize()

        params = {"name": name, "arguments": arguments if arguments is not None else {}}
        result = self._send_request("tools/call", params)

        if return_full_result:
            return result

        content = result.get("content", [])
        if content and len(content) == 1 and content[0].get("type") == "text":
            return content[0].get("text", "")
        return content


def cmd_list_tools(args):
    """List available MCP tools."""
    client = None
    try:
        client = AtlassianMCPClient()
        tools = client.list_tools()

        output = {
            "tools": [
                {
                    "name": t.get("name"),
                    "description": t.get("description", "")[:100],
                }
                for t in tools
            ],
            "count": len(tools),
        }
        yaml_output(output)

    except AuthenticationError as e:
        yaml.dump({"error": str(e)}, sys.stderr)
        sys.exit(1)
    except MCPError as e:
        yaml.dump({"error": str(e)}, sys.stderr)
        sys.exit(1)
    finally:
        if client:
            client.close()


def cmd_call_tool(args):
    """Call an MCP tool."""
    client = None
    try:
        client = AtlassianMCPClient()

        arguments = None
        if args.arguments:
            try:
                arguments = json.loads(args.arguments)
            except json.JSONDecodeError as e:
                yaml.dump({"error": f"Invalid JSON arguments: {e}"}, sys.stderr)
                sys.exit(1)

        result = client.call_tool(args.tool_name, arguments)
        yaml_output({"result": result})

    except AuthenticationError as e:
        yaml.dump({"error": str(e)}, sys.stderr)
        sys.exit(1)
    except MCPError as e:
        yaml.dump({"error": str(e)}, sys.stderr)
        sys.exit(1)
    finally:
        if client:
            client.close()


def cmd_test(args):
    """Test MCP connection and list tools."""
    client = None
    try:
        print("Testing MCP connection to Atlassian...")

        client = AtlassianMCPClient()
        print(f"Token found: {client.token[:20]}...")

        print("\nInitializing MCP session...")
        caps = client.initialize()
        print(f"Session ID: {client.session_id}")
        print(f"Server: {caps.get('serverInfo', {})}")
        print(f"Protocol: {caps.get('protocolVersion', 'unknown')}")

        print("\nListing tools...")
        tools = client.list_tools()

        print(f"\nFound {len(tools)} tools:")
        for tool in tools:
            print(f"  - {tool.get('name')}: {tool.get('description', '')[:60]}...")

    except AuthenticationError as e:
        print(f"Auth error: {e}", file=sys.stderr)
        sys.exit(1)
    except MCPError as e:
        print(f"MCP error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if client:
            client.close()


def main():
    parser = argparse.ArgumentParser(
        description="Atlassian MCP client",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    subparsers.add_parser("list-tools", help="List available MCP tools")

    call_parser = subparsers.add_parser("call", help="Call an MCP tool")
    call_parser.add_argument("tool_name", help="Name of the tool to call")
    call_parser.add_argument("arguments", nargs="?", help="Tool arguments as JSON string")

    subparsers.add_parser("test", help="Test MCP connection")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "list-tools": cmd_list_tools,
        "call": cmd_call_tool,
        "test": cmd_test,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
