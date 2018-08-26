import marcalyx
import xml.etree.ElementTree as ET
tree = ET.parse('tests/xml/1027474578.xml')
root = tree.getroot()
r = marcalyx.Record(root)


def test_leader():
    assert r.leader == '00000cam a2200000Mi 4500'

def test_fields():
    f = r.fields
    ftypes = list(set([type(field) for field in r.fields]))
    assert isinstance(f, list)
    assert len(ftypes) == 2
    assert marcalyx.marcalyx.ControlField in ftypes
    assert marcalyx.marcalyx.DataField in ftypes
    
def test_getting_a_field():
    f = r.field('245')
    assert isinstance(f, list)
    assert len(f) == 1
    assert f[0].tag == '245'

def test_getting_field_by_index():
    assert r.field('245') == r['245']

    
def test_getting_control_and_data_fields():
    print(type(r['001'][0]))
    assert isinstance(r['001'][0], marcalyx.marcalyx.ControlField)
    assert isinstance(r['245'][0], marcalyx.marcalyx.DataField)

def test_title_statement():
    assert str(r.titleStatement()) == '245 10$aKindred /$cOctavia E. Butler.'


def test_datafield_value():
    assert r.titleStatement().value() == 'Kindred / Octavia E. Butler.'
