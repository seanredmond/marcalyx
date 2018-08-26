import marcalyx
import pytest
import xml.etree.ElementTree as ET

@pytest.fixture()
def kindred():
    tree = ET.parse('tests/xml/1027474578.xml')
    root = tree.getroot()
    return marcalyx.Record(root)


@pytest.fixture()
def quilt():
    tree = ET.parse('tests/xml/10705.xml')
    root = tree.getroot()
    return marcalyx.Record(root)


def test_leader(kindred):
    assert kindred.leader == '00000cam a2200000Mi 4500'

def test_fields(kindred):
    f = kindred.fields
    ftypes = list(set([type(field) for field in kindred.fields]))
    assert isinstance(f, list)
    assert len(ftypes) == 2
    assert marcalyx.marcalyx.ControlField in ftypes
    assert marcalyx.marcalyx.DataField in ftypes


def test_subfield(kindred):
    s = kindred.subfield('650', 'a')
    assert isinstance(s, list)
    assert len(s) == 2
    assert list(set([type(sub) for sub in s])) == [marcalyx.marcalyx.SubField]


def test_subfield_when_some_are_empty(kindred):
    # There is one 651 field with an $x and one without
    s = kindred.subfield("651", "x")
    assert isinstance(s, list)
    assert len(s) == 1


def test_subfields_when_all_should_be_empy(kindred):
    s = kindred.subfield("650", "9")
    assert isinstance(s, list)
    assert len(s) == 0


def test_getting_a_field(kindred):
    f = kindred.field('245')
    assert isinstance(f, list)
    assert len(f) == 1
    assert f[0].tag == '245'


def test_getting_field_by_index(kindred):
    assert kindred.field('245') == kindred['245']

    
def test_getting_control_and_data_fields(kindred):
    assert isinstance(kindred['001'][0], marcalyx.marcalyx.ControlField)
    assert isinstance(kindred['245'][0], marcalyx.marcalyx.DataField)


def test_title_statement(kindred):
    assert str(kindred.titleStatement()) == \
        '245 10$aKindred /$cOctavia E. Butler.'


def test_datafield_value(kindred):
    assert kindred.titleStatement().value() == 'Kindred / Octavia E. Butler.'


def test_main_entry(kindred, quilt):
    k = kindred.mainEntry()
    q = quilt.mainEntry()

    assert isinstance(k, marcalyx.marcalyx.DataField)
    assert k.tag == '100'

    assert isinstance(q, marcalyx.marcalyx.DataField)
    assert q.tag == '111'
