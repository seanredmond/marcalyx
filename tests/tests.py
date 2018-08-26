import marcalyx
import xml.etree.ElementTree as ET
tree = ET.parse('tests/xml/1027474578.xml')
root = tree.getroot()
r = marcalyx.Record(root)

def test_title_statement():
    assert str(r.titleStatement()) == '245 10$aKindred /$cOctavia E. Butler.'


def test_datafield_value():
    assert r.titleStatement().value() == 'Kindred / Octavia E. Butler.'
