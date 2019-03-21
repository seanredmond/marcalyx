import marcalyx
import pytest
import xml.etree.ElementTree as ET


@pytest.fixture()
def dataf():
    tree = ET.parse('tests/xml/1027474578.xml')
    root = tree.getroot()
    return marcalyx.Record(root)['100'][0]


def test_tag(dataf):
    assert dataf.tag == '100'


def test_value(dataf):
    assert dataf.value == 'Butler, Octavia Estelle (1947-2006). aut'


def test_to_string(dataf):
    assert str(dataf) == '100 1#$aButler, Octavia Estelle$d(1947-2006).$4aut'


def test_subfields(dataf):
    assert isinstance(dataf.subfields, list)
    assert len(dataf.subfields) == 3
