# -*- coding: utf-8 -*-

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


@pytest.fixture()
def binti():
    tree = ET.parse('tests/xml/973807354.xml')
    root = tree.getroot()
    return marcalyx.Record(root)


@pytest.fixture()
def wrinkle():
    tree = ET.parse('tests/xml/14026028.xml')
    root = tree.getroot()
    return marcalyx.Record(root[0])


@pytest.fixture()
def marner():
    tree = ET.parse('tests/xml/2971.xml')
    root = tree.getroot()
    return marcalyx.Record(root)

@pytest.fixture()
def russian():
    tree = ET.parse('tests/xml/528635.xml')
    root = tree.getroot()
    return marcalyx.Record(root)


@pytest.fixture()
def xenophon():
    tree = ET.parse('tests/xml/3863.xml')
    root = tree.getroot()
    return marcalyx.Record(root)


@pytest.fixture()
def fissures():
    tree = ET.parse('tests/xml/53998.xml')
    root = tree.getroot()
    return marcalyx.Record(root)


def test_leader(kindred):
    assert kindred.leader == '00000cam a2200000Mi 4500'

    
def test_subfield(kindred):
    s = kindred.subfield('650', 'a')
    assert isinstance(s, list)
    assert len(s) == 2
    assert list(
        set([isinstance(sub, marcalyx.marcalyx.SubField) for sub in s])
    ) == [True]


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


def test_control_fields(kindred):
    ctrl = kindred.controlFields()
    assert isinstance(ctrl, list)
    assert list(
        set([isinstance(f, marcalyx.marcalyx.ControlField) for f in ctrl])
    ) == [True]
    assert len(ctrl) == 2
    assert ctrl[0],tag == '001'
    assert ctrl[-1].tag == '008'


def test_codes(kindred):
    codes = kindred.codes()
    assert isinstance(codes, list)
    assert len(codes) == 2
    assert codes[0].tag == "020"
    assert codes[0].value() == '9781472214812'


def test_titles(binti):
    t = binti.titles()
    assert isinstance(t, list)
    assert len(t) == 2
    assert t[0].tag == '245'
    assert t[-1].tag == '246'
    assert t[0].value() == 'Binti : the night masquerade / Nnedi Okorafor.'
    assert t[-1].value() == 'Night masquerade'


def test_editions(wrinkle):
    edition = wrinkle.edition()
    assert isinstance(edition, list)
    assert len(edition) ==  1
    assert edition[0].tag == '260'
    assert edition[0].value() == \
        'Harmondsworth, Eng. : Penguin Books, 1967, c1962.'


def test_description(wrinkle):
    description = wrinkle.description()
    assert isinstance(description, list)
    assert len(description) == 1
    assert description[0].tag == '300'
    assert description[0].value() == '184 p. ; 18 cm.'


def test_series(marner):
    series = marner.series()
    assert isinstance(series, list)
    assert len(series) == 1
    assert series[0].tag == '490'
    assert series[0].value() == 'Standard literature series ; no. 43'


def test_notes(quilt):
    notes = quilt.notes()
    assert isinstance(notes, list)
    assert len(notes) == 3
    assert notes[0].tag == '500'
    assert notes[0].value() == '"Millennium celebration."'


def test_subjects(kindred):
    subjects = kindred.subjects()
    assert isinstance(subjects, list)
    assert len(subjects) == 4
    assert subjects[0].tag == '650'
    assert subjects[0].value() == 'African American women Fiction.'


def test_added_entries(quilt):
    added = quilt.addedEntries()
    assert isinstance(added, list)
    assert len(added) == 2
    assert added[0].tag == '700'
    assert added[-1].tag == '710'
    assert added[0].value() == 'Browning, Bonnie K., 1944-'
    assert added[-1].value() == 'American Quilter\'s Society.'


def test_linking(russian):
    links = russian.linking()
    assert isinstance(links, list)
    assert len(links) == 1
    assert links[0].tag == '776'
    assert links[0].value() == 'Original (DLC)   61060095'


def test_series_added(xenophon):
    series = xenophon.seriesAdded()
    assert len(series) == 1
    assert series[0].tag == '810'
    assert series[0].value() == \
        'Cornell University. Cornell studies in classical philology ; no. 11.'


def test_holdings(binti):
    holdings = binti.holdings()
    assert len(holdings) == 1
    assert holdings[0].tag == '880'
    assert holdings[0].value() == '264-00 © 2017'


def test_lccn(quilt, kindred):
    assert quilt.lccn() == "   00010705 "
    assert kindred.lccn() is None
    

def test_isbns(kindred):
    assert isinstance(kindred.isbns(), list)
    assert kindred.isbns() == ['9781472214812', '1472214811']


def test_issns(fissures):
    assert isinstance(fissures.issns(), list)
    assert fissures.issns() == ['1572733691 (pbk.)']
