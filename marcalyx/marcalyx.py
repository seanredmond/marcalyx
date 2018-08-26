NS = {'marc': 'http://www.loc.gov/MARC21/slim'}
class Record:
    def __init__(self, node):
        self.node = node
        self.leader = node.find('marc:leader', NS).text
        self.fields = [ControlField(f) for f in
                       node.findall('marc:controlfield', NS)] + \
                       [DataField(f) for f in
                       node.findall('marc:datafield', NS)]


    def titleStatement(self):
        return self.field('245')[0]

    
    def field(self, tag):
        return [f for f in self.fields if f.tag == tag]


    def subfield(self, tag, code):
        return [g for h in
                [f.subfield(code) for f in self.field(tag)]
                for g in h]


    def __getitem__(self, tag):
        return self.field(tag)

    
class ControlField:
    def __init__(self, node):
        self.node = node
        self.tag = node.attrib['tag']
        self.value = node.text


    def __repr__(self):
        return "%s   %s" % (self.tag, self.value,)


class DataField:
    def __init__(self, node):
        self.node = node
        self.tag = node.attrib['tag']
        self.ind1 = node.attrib['ind1']
        self.ind2 = node.attrib['ind2']
        self.subfields = [SubField(s) for s in
                          node.findall('marc:subfield', NS)]


    def subfield(self, code):
        return [s for s in self.subfields if s.code == code]
        
    def value(self):
        return ' '.join([s.value for s in self.subfields])

    
    def ind_to_s(self, i):
        if i == ' ':
            return '#'

        return i
    
    def __repr__(self):
        return "%s %s%s%s" % (self.tag,
                              self.ind_to_s(self.ind1),
                              self.ind_to_s(self.ind2),
                              ''.join([str(s) for s in self.subfields]),)


class SubField:
    def __init__(self, node):
        self.code = node.attrib['code']
        self.value = node.text

    def __repr__(self):
        return "$%s%s" % (self.code, self.value,)
