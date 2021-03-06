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


def test_subfield(dataf):
    subf = dataf.subfield('a')
    assert isinstance(subf, list)
    assert isinstance(subf[0], marcalyx.marcalyx.SubField)
    assert subf[0].value == 'Butler, Octavia Estelle'


def test_subfield_getitem(dataf):
    subf = dataf['a']
    assert isinstance(subf, list)
    assert isinstance(subf[0], marcalyx.marcalyx.SubField)
    assert subf[0].value == 'Butler, Octavia Estelle'
