#!/usr/bin/env python3
"""
MCP Client for interacting with the KaitoMCPServer
This client demonstrates how to list resources and call tools.
"""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    """Main client function to interact with the MCP server"""

    # Server parameters - running the server via main.py
    server_params = StdioServerParameters(command="mcp", args=["run", "server.py"])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()

            print("🚀 Connected to KaitoMCPServer!")
            print("=" * 50)

            # List available tools
            print("\n📋 Available Tools:")
            print("-" * 20)
            tools_result = await session.list_tools()

            if tools_result.tools:
                for tool in tools_result.tools:
                    print(f"• {tool.name}: {tool.description}")
                    if hasattr(tool, "inputSchema") and tool.inputSchema:
                        properties = tool.inputSchema.get("properties", {})
                        if properties:
                            print(f"  Parameters: {list(properties.keys())}")
            else:
                print("  No tools available")

            # List available resources
            print("\n📚 Available Resources:")
            print("-" * 22)
            resources_result = await session.list_resources()

            if resources_result.resources:
                for resource in resources_result.resources:
                    print(f"• {resource.uri}: {resource.name}")
                    if hasattr(resource, "description") and resource.description:
                        print(f"  Description: {resource.description}")
            else:
                print("  No resources available")

            # Demonstrate calling the add tool
            print("\n🔧 Testing Tools:")
            print("-" * 16)

            try:
                # Call the add tool with some numbers
                add_result = await session.call_tool("add", {"a": 15, "b": 27})
                print(f"add(15, 27) = {add_result.content[0].text}")

                # Call add tool with different numbers
                add_result2 = await session.call_tool("add", {"a": 100, "b": 50})
                print(f"add(100, 50) = {add_result2.content[0].text}")

            except Exception as e:
                print(f"Error calling add tool: {e}")

            # Demonstrate reading resources
            print("\n📖 Testing Resources:")
            print("-" * 19)

            try:
                # Read the greeting resource with different names
                names_to_try = ["Alice", "Bob", "World"]

                for name in names_to_try:
                    resource_uri = f"greeting://{name}"
                    try:
                        resource_result = await session.read_resource(resource_uri)
                        if resource_result.contents:
                            content = resource_result.contents[0]
                            print(f"Resource {resource_uri}: {content.text}")
                    except Exception as e:
                        print(f"Error reading resource {resource_uri}: {e}")

            except Exception as e:
                print(f"Error testing resources: {e}")

            print("\n✅ Client testing completed!")


def run_client():
    """Convenience function to run the client"""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Client interrupted by user")
    except Exception as e:
        print(f"❌ Client error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    run_client()
