import marcalyx
import pytest
import xml.etree.ElementTree as ET

@pytest.fixture()
def lengle_node():
    tree = ET.parse('tests/xml/14026028.xml')
    root = tree.getroot()


@pytest.fixture()
def lengle():
    tree = ET.parse('tests/xml/14026028.xml')
    root = tree.getroot()
    return marcalyx.Collection(root)


def test_creation(lengle_node):
    assert isinstance(marcalyx.Collection(lengle_node),
                      marcalyx.marcalyx.Collection)


def test_records(lengle):
    records = lengle.records()
    assert isinstance(records, list)
    assert len(records) == 1
    assert list(set([type(r) for r in records])) == [marcalyx.marcalyx.Record]
