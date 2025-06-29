
import pytest
from mcp_server import _validate_libvirt_xml as validate_libvirt_xml

def test_valid_xml():
    xml_string = "<domain type='kvm'><name>test</name></domain>"
    result = validate_libvirt_xml(xml_string=xml_string)
    assert result["returncode"] == 0

def test_invalid_xml():
    xml_string = "<domain type='kvm'></domain>"
    result = validate_libvirt_xml(xml_string=xml_string)
    assert result["returncode"] != 0
