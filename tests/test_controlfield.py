import marcalyx
import pytest
import xml.etree.ElementTree as ET


@pytest.fixture()
def ctrl():
    tree = ET.parse('tests/xml/1027474578.xml')
    root = tree.getroot()
    return marcalyx.Record(root)['001'][0]


def test_tag(ctrl):
    assert ctrl.tag == '001'


def test_value(ctrl):
    assert ctrl.value == '1027474578'


def test_to_string(ctrl):
    assert str(ctrl) == '001   1027474578'


def test_subfields(ctrl):
    assert isinstance(ctrl.subfields, list)
    assert len(ctrl.subfields) == 0
