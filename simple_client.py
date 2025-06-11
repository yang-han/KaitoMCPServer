#!/usr/bin/env python3
"""
Simple MCP Client for testing KaitoMCPServer
This demonstrates basic interaction with the MCP server.
"""

import asyncio
import subprocess
import json
import sys
from pathlib import Path


async def test_server_directly():
    """Test the server by importing it directly"""
    print("🧪 Testing server directly...")
    
    # Import the server
    from server import mcp
    
    print("✅ Server imported successfully!")
    print(f"Server name: {mcp.name}")
    
    # Get tools info
    print("\n📋 Available Tools:")
    print("-" * 20)
    
    # The FastMCP server should have tools registered
    if hasattr(mcp, '_tools'):
        for tool_name, tool_info in mcp._tools.items():
            print(f"• {tool_name}: {tool_info.get('description', 'No description')}")
    
    # Test the add function directly
    print("\n🔧 Testing add function directly:")
    print("-" * 32)
    
    from server import add
    result1 = add(15, 27)
    result2 = add(100, 50)
    print(f"add(15, 27) = {result1}")
    print(f"add(100, 50) = {result2}")
    
    # Test the greeting function directly
    print("\n📖 Testing greeting function directly:")
    print("-" * 36)
    
    from server import get_greeting
    greeting1 = get_greeting("Alice")
    greeting2 = get_greeting("Bob")
    greeting3 = get_greeting("World")
    print(f"get_greeting('Alice') = {greeting1}")
    print(f"get_greeting('Bob') = {greeting2}")
    print(f"get_greeting('World') = {greeting3}")


def run_server_test():
    """Run the server test"""
    try:
        print("🚀 KaitoMCPServer Client Test")
        print("=" * 30)
        
        asyncio.run(test_server_directly())
        
        print("\n" + "=" * 30)
        print("✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


def show_usage():
    """Show usage instructions"""
    print("""
🔧 KaitoMCPServer Client

Usage:
  python client.py              - Run direct server tests
  python client.py --help       - Show this help message

To run the actual MCP server:
  python main.py                - Start the MCP server
  
To test with MCP protocol:
  # In one terminal:
  python main.py
  
  # In another terminal:
  python client.py
""")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
        show_usage()
    else:
        run_server_test()
