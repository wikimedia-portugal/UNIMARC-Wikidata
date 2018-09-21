import re

from mapper import wdconversions


class endo:
    def __init__(self, data):
        self.data = data
        self.lpt = self.lpt()
        self.dpt = self.dpt()

    def lpt(self):
        return (self.data.findAll(tag="200")[0].find(code="a").contents[0])

    def dpt(self):
        return self.data.findAll(tag="330")[0].find(code="a").contents[0]

    def len(self):
        return None

    def den(self):
        return None

    def p31(self):
        return None

    def p495(self):
        try:
            return self.data.findAll(tag="102")[0].find(code="a").contents
        except:
            return None

    def p571(self):
        return self.data.findAll(tag="210")[0].find(code="d").contents[0]

    def p276(self):
        return None

    def p195(self):
        return None

    def p136(self):
        return None

    def p170(self):
        # TODO check if this is the correct unimarc tag, and make the name composition
        return self.data.findAll(tag="700")


    def p204x(self):
        size = self.data.findAll(tag="215")[0].find(code="d").contents

        dims = re.search('(\d+(?:[.,]\d+)?)(?:\s*([cd]?m))?\s*x\s*(\d+(?:[.,]\d+)?)\s*([cd]?m)', size[0])
        p204x = dict()
        print(dims.groups())
        if not dims.group(2) and dims.group(4):
            units = wdconversions.si()[dims.group(4)]

        if dims:
            p204x['P2048'] = "{0}{1}".format(dims.group(1).replace(",", "."), units)
            p204x['P2049'] = "{0}{1}".format(dims.group(3).replace(",", "."), units)
        return p204x
    def p2048(self):
        return self.p204x()['P2048']
    def p2049(self):
        return self.p204x()['P2049']
    def p186(self):
        # TODO improve material detection, and material dict on wdconversions
        _data = self.data.findAll(tag="215")[0].find(code="c").contents[0]
        p186 = dict()

        if re.search('acr[ií]lico .+ tela', _data):
            p186['P186-tela'] = wdconversions.materials()['tela']
            p186['P186-acrílico'] = wdconversions.materials()['acrilico']

        elif re.search('[oó]leo .+ tela', _data):
            p186['P186-tela'] = wdconversions.materials()['tela']
            p186['P186-oleo'] = wdconversions.materials()['oleo']

        return p186

    def p217(self):

        _data = self.data.findAll(tag="966")[0].find(code="s").contents[0]
        return _data

    def p973(self):

        _data = self.data.findAll(tag="003")[0].contents

        return _data

    def p5691(self):

        _data = self.data.findAll(tag="856")[0].find(code="u").contents[0].split(".pt/")
        return _data[1]
