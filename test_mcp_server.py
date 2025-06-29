
import pytest
from mcp_server import _validate_libvirt_xml

@pytest.mark.parametrize("xml_string, expected_return_code", [
    ("<domain type='kvm'><name>test</name></domain>", 0),
    ("<domain type='kvm'></domain>", 3),
])
def test_virt_xml_validate(xml_string, expected_return_code):
    """Tests the XML validation with different inputs."""
    result = _validate_libvirt_xml(xml_string)
    assert result["returncode"] == expected_return_code
