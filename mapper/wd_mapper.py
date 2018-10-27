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
        try:
            return self.data.findAll(tag="330")[0].find(code="a").contents[0]
        except:
            return None

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
        # p571_data = ""
        #
        # # return self.data.findAll(tag="210")[0].find(code="d").contents[0]
        # st = self.data.findAll(tag="210")[0].find(code="d").contents[0]
        # print(st)
        # p = re.search("^\d{4}$", str(st))
        # date_rx = "^\[(\d{2})\-\-\]$"
        # date_rx_2 = "^\[(\d{4})(?:\?)\]$"
        # date_rx_3 = "^\[(\d{2})\-\-(?:\?)?\]$"
        # qal = dict()
        # qal["qal1480"] = ""
        # if p:
        #     wdate = "+{}-00-00T00:00:00Z/9".format(p.group())
        # elif re.search(date_rx, str(st)):
        #     p = re.search(date_rx, str(st))
        #     print(p)
        #     wdate = "+{}00-00-00T00:00:00Z/9".format((int(p.group(1)) + 1))
        #     qal["qal1480"] = "Q18122778"
        # elif re.search(date_rx_2, str(st)):
        #     p = re.search(date_rx_2, str(st))
        #     wdate = "+{}-00-00T00:00:00Z/9".format((int(p.group(1)) + 1))
        #     qal["qal1480"] = "Q18122778"
        # elif re.search(date_rx_3, str(st)):
        #     p = re.search(date_rx_3, str(st))
        #     wdate = "+{}00-00-00T00:00:00Z/9".format((int(p.group(1)) + 1))
        #     qal["qal1480"] = "Q21097017"
        #
        # else:
        #     wdate = st
        qal = dict()

        st = self.data.findAll(tag="210")[0].find(code="d").contents[0]
        qal = dict()
        qal["qal1480"] = ""
        date_lower = ""
        date_upper = ""
        wdate = ""
        _year = re.search("^\d{4}$", str(st))
        _year_unc = re.search("^\[(\d{4})(?:\?)\]$", str(st))
        _year_unc_2 = re.search("^\[(\d{4})\]$", str(st))

        _cent_unc = re.search("^\[(\d{2})\-\-(?:\?)\]$", str(st))
        _cent = re.search("^\[(\d{2})\-\-\]$", str(st))
        _between = re.search("\[entre (\d{4}) e (\d{4})\?\]", st)

        if _year:
            wdate = "+{}-00-00T00:00:00Z/9".format(_year.group())


        elif _year_unc:
            wdate = "+{}-00-00T00:00:00Z/9".format((int(_year_unc.group(1))))

            qal["qal1480"] = "Q18122778"
        elif _year_unc_2:
            wdate = "+{}-00-00T00:00:00Z/9".format((int(_year_unc_2.group(1))))

            qal["qal1480"] = "Q21097017"
        elif _cent:
            wdate = "+{}00-00-00T00:00:00Z/9".format((int(_cent.group(1)) + 1))
            qal["qal1480"] = "Q21097017"

        elif _cent_unc:
            wdate = "+{}00-00-00T00:00:00Z/9".format((int(_cent_unc.group(1)) + 1))
            qal["qal1480"] = "Q18122778"



        elif _between:
            _wdate1 = _between.group(1)
            _wdate2 = _between.group(2)
            date_lower = "+{}-00-00T00:00:00Z/9".format(_wdate1)
            date_upper = "+{}-00-00T00:00:00Z/9".format(_wdate2)
            qal["qal1480"] = "Q18122778"

        else:
            wdate = st

        s = qal["qal1480"]

        return st, wdate, s, date_lower, date_upper

    def p276(self):
        return None

    def p195(self):
        return None

    def p136(self):
        return None

    def p170(self):
        # TODO check if this is the correct unimarc tag, and make the name composition
        info = self.data.findAll(tag="700")
        # try:
        #     print("700 3 ", self.data.findAll(tag="700")[0].find(code="3").contents[0])
        # except:
        #     pass

        if info:
            auth_purl = None
            f_name = self.data.findAll(tag="700")[0].find(code="a").contents[0]
            s_name = self.data.findAll(tag="700")[0].find(code="b").contents[0]

            if f_name and s_name:
                name = "{} {}".format(s_name, f_name)
            else:
                name = s_name

            if self.data.findAll(tag="700")[0].find(code="3").contents[0]:
                auth_purl = "http://urn.bn.pt/nca/unimarc-authorities/txt?id={}".format(
                    self.data.findAll(tag="700")[0].find(code="3").contents[0])

            return name, auth_purl
        else:
            return None, None

    def p204x(self):
        size = self.data.findAll(tag="215")[0].find(code="d").contents

        dims = re.search('(\d+(?:[.,]\d+)?)(?:\s*([cd]?m))?\s*x\s*(\d+(?:[.,]\d+)?)\s*([cd]?m)', size[0])
        p204x = dict()
        # print(dims.groups())
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

    def p204y(self):
        p204y = dict()
        p204y['P2048'] = None
        p204y['P2049'] = None
        try:
            size = self.data.findAll(tag="307")[0].find(code="a").contents

            dims = re.search('(\d+(?:[.,]\d+)?)(?:\s*([cd]?m))?\s*x\s*(\d+(?:[.,]\d+)?)\s*([cd]?m)', size[0])

            # print(dims.groups())
            if not dims.group(2) and dims.group(4):
                units = wdconversions.si()[dims.group(4)]

            if dims:
                p204y['P2048'] = "{0}{1}".format(dims.group(1).replace(",", "."), units)
                p204y['P2049'] = "{0}{1}".format(dims.group(3).replace(",", "."), units)
            else:
                pass
        except:
            pass

        return p204y['P2048'], p204y['P2049']

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
        elif re.search('[oó]leo .+ madeira', _data):
            p186['P186-madeira'] = wdconversions.materials()['madeira']
            p186['P186-oleo'] = wdconversions.materials()['oleo']
        elif re.search('[oó]leo .+ cobre', _data):
            p186['P186-cobre'] = wdconversions.materials()['cobre']
            p186['P186-oleo'] = wdconversions.materials()['oleo']

        materials = list()
        for i in p186.keys():
            materials.append(p186[i])

        return p186, materials

    def p195(self):
        # print("col: !", self.data.findAll(tag="225")[0])
        col = list()

        if self.data.findAll(tag="225")[0].find(code="i"):
            # print ("!!!!!!!!!!!-> ", self.data.findAll(tag="225")[0].find(code="i").contents[0])
            _temp = self.data.findAll(tag="225")[0].find(code="i").contents[0]
            # print (_temp)
            # print ( wdconversions.colecao()[_temp])
            col.append(wdconversions.colecao()[_temp])

        if self.data.findAll(tag="225")[0].find(code="a"):
            _temp = self.data.findAll(tag="225")[0].find(code="a").contents[0].replace(".","")
            print (wdconversions.colecao()[_temp])
            col.append( wdconversions.colecao()[_temp])
        if len(col) == 1:
            col.append(None)

        return col[0], col[1]

    def p217(self):

        _data = self.data.findAll(tag="966")[0].find(code="s").contents[0]
        return _data

    def p973(self):

        _data = self.data.findAll(tag="003")[0].contents

        return _data[0]

    def p5691(self):

        _data = self.data.findAll(tag="856")[0].find(code="u").contents[0].split(".pt/")
        return _data[1]


class comms:
    def __init__(self, data):
        self.data = data

    def c304(self):
        _data = list()
        for i in self.data.findAll(tag="304"):
            _data.append("{}<br/>".format(i.find(code="a").contents[0]))
        return "".join(_data)

    def c306(self):
        _data = self.data.findAll(tag="306")[0].find(code="a").contents[0]
        return _data

    def c307(self):
        _data = self.data.findAll(tag="307")[0].find(code="a").contents[0]
        return _data

    def inv(self):
        _data = self.data.findAll(tag="966")[0].find(code="s").contents[0]
        return _data

    def u_title(self):
        _data = self.data.findAll(tag="200")[0].find(code="a").contents[0]
        return _data

    def c321a(self):
        _data = list()
        for i in self.data.findAll(tag="321"):
            _data.append("{}<br/>".format(i.find(code="a").contents[0]))
        return "".join(_data)

    def c321all(self):
        c321_all = ""
        if len(self.data.findAll(tag="321")) == 2:
            c321_all = self.data.findAll(tag="321")[0].get_text()

            _tag321 = list()
            for i in self.data.findAll(tag="321")[1]:
                _tag321.append(i.get_text())

            _c321all = "<br/>{0} {1}".format(_tag321[0], _tag321[1])
            c321_all += _c321all
        return c321_all
