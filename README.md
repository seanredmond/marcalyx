# Marcalyx

[![PyPi Version](https://badge.fury.io/py/marcalyx.svg)][pypi]
[![Build Status](http://img.shields.io/travis/seanredmond/marcalyx.svg)][travis]

[travis]: http://travis-ci.org/seanredmond/marcalyx
[pypi]: https://pypi.org/project/marcalyx


Simple python interface for reading
[MARC-XML](https://www.loc.gov/standards/marcxml/)


## Installation

    pip install marcalyx
    
## Usage

Import the package

    >>> import marcalyx

Marcalyx works on `xml.etree.ElementTree.Element` objects (or compatible), so
you will need to parse the XML before passing it to a Marcalyx object. For
instance, given a file containing a single `<record>`:

    >>> import xml.etree.ElementTree as ET
    
or, using `lxml`:

    >>> import lxml.etree as ET
    
then:

    >>> tree = ET.parse('tests/xml/1027474578.xml')
    >>> record_element = tree.getroot()
    >>> marc = marcalyx.Record(record_element)

If the XML contains a `<collection>` of Records you would instead create a `marcalyx.Collection` object, from which you can get the records:

    >>> coll = marcalyx.Collection(collection_element)
    >>> marc = coll.records()[0]

## Fields

Once you have a record, you can access the fields by tag (always use the 3-character string, for example, "001", "010", "100"):

    >>> marc.field("245")
    [245 10$aKindred /$cOctavia E. Butler.]
    
Or, more simply:

    >>> marc["245"]
    [245 10$aKindred /$cOctavia E. Butler.]
    
Fields are always returned as an array when accessed by tag (but not necessarily from the convenience methods, below). Fields are either a ControlField:

    >>> type(m["008"][0])
    <class 'marcalyx.marcalyx.ControlField'>
    
Or a DataField:

    >>> type(m["245"][0])
    <class 'marcalyx.marcalyx.DataField'>

All fields have a `tag` and a `value`:

    >>> m["008"][0].tag
    '008'
    >>> m["245"][0].tag
    '245'
    >>> m["008"][0].value
    '180306r20141979xxk    g      000 j eng d'
    >>> m["245"][0].value
    'Kindred / Octavia E. Butler.'

Data fields have their two "indicators":

    >>> m["245"][0].ind1
    '1'
    >>> m["245"][0].ind2
    '0'
    
And subfields, which can be accessed via the `subfield()` method, which returns an array:

    >>> m["245"][0].subfield('a')
    [$aKindred /]
    
As with fields, you can get subfields via subscript:

    >>> m["245"][0]['a']
    [$aKindred /]
    
You can use a tuple containing a field tag and subfield code as a subscript to
get a flat list of all the subfields with that code (if any) of all the fields
with that tag (if any):

    >>> m[('650','a')]
    [$aAfrican American women, $aTime travel]

## `value` vs. `str`

The string representation of a field is formatted in the conventional way, showing the indicators and subfields:

    >>> str(m["245"][0])
    '245 10$aKindred /$cOctavia E. Butler.'
    
The `value` is formatted for display:

    >>> m["245"][0].value
    'Kindred / Octavia E. Butler.'

## Subfields

Subfields have codes, values, and string representations:

    >>> m["245"][0].subfield("a")[0].code
    'a'
    >>> m["245"][0].subfield("a")[0].value
    'Kindred /'
    >>> str(m["245"][0].subfield("a")[0])
    '$aKindred /'
    
## Convenience methods

There are several methods to make it easier to get single fields or categories
of fields. `mainEntry()` will return whichever of the 1XX fields the record has
(as a `DataField`, not an array):

    >>> m.mainEntry()
    100 1#$aButler, Octavia Estelle$d(1947-2006).$4aut

`#titleStatement` gets the 245 field (again, as a `DataField` and not an array):

    >>> m.titleStatement()
    245 10$aKindred /$cOctavia E. Butler.

There are also methods to get an array of each of the main categories of
fields. Each of these returns an array of all the fields in the record of the
given category:

    >>> marc.controlFields() # 00X
    >>> marc.codes()         # 01X-09X
    >>> marc.titles()        # 20X-24X
    >>> marc.edition()       # 25X-28X
    >>> marc.description()   # 3XX
    >>> marc.series()        # 4XX
    >>> marc.notes()         # 5XX
    >>> marc.subjects()      # 6XX
    >>> marc.addedEntries()  # 70X-75X
    >>> marc.linking()       # 76X-78X
    >>> marc.seriesAdded()   # 80X-83X
    >>> marc.holdings()      # 841-88X

Some common numbers have convenience methods:

    > record.lccn       # 010$a, String or nil
    > record.isbns      # 020$a, Array of Strings, or []
    > record.issns      # 022$a, Array of Strings, or []

## Leader

You can get the record leader:

    >>> marc.leader
    '00000cam a2200000Mi 4500'

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/seanredmond/marcalyx. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Lccnorm project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/seanredmond/marcalyx/blob/master/CODE_OF_CONDUCT.md).
