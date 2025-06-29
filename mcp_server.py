import os
import tempfile
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-server")


def _validate_libvirt_xml(xml_string: str) -> dict:
    with tempfile.NamedTemporaryFile("w+", suffix=".xml", delete=False) as tmp:
        tmp.write(xml_string)
        tmp.flush()
        tmp_path = tmp.name
    try:
        result = subprocess.run(
            ["virt-xml-validate", tmp_path],
            capture_output=True,
            text=True,
            check=False
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    finally:
        os.remove(tmp_path)

@mcp.tool()
async def validate_libvirt_xml(xml_string: str) -> dict:
    """
    Validates a libvirt XML string using virt-xml-validate.
    Returns the result of the validation.
    """
    return _validate_libvirt_xml(xml_string)


if __name__ == "__main__":
    mcp.run(transport=os.environ.get("MCP_TRANSPORT", "stdio"))
