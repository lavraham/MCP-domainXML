import os
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-server")


@mcp.tool()
async def validate_libvirt_xml(xml_string: str) -> dict:
    """
    Validates a libvirt XML string using virt-xml-validate.
    Returns the result of the validation.
    """
    result = subprocess.run(
        ["virt-xml-validate", "-"],
        input=xml_string,
        capture_output=True,
        text=True,
        check=False
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }


if __name__ == "__main__":
    mcp.run(transport=os.environ.get("MCP_TRANSPORT", "stdio"))
