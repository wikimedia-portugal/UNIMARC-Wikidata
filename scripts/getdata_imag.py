import requests
from bs4 import BeautifulSoup
from mapper import wd_mapper as mp
import csv


def get(purl):
    url = 'http://urn.bn.pt/purl/unimarc/xml?id={}&agente=urn.porbase.org'.format(purl)
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content, 'lxml-xml')

    # maped = mp.endo(soup)
    #
    # p31 = "Q3305213"
    # p921 = ""
    # p1684 = ""
    # p495 = "Q45"
    #
    # # data = (maped.lpt, ";",maped.dpt, ";",maped.len(), ";",maped.den(), ";",p31, ";",p495, ";",maped.p571(), ";",maped.p276(), ";",maped.p195(), ";",maped.p195(), ";",maped.p136(), ";",maped.p170(), ";",maped.p2049(), ";",maped.p2048(), ";",None, ";",None, ";",maped.p186(), ";",maped.p186(), ";",maped.p217(), ";",p921, ";",p921, ";",maped.p973(), ";",maped.p5691(), ";",p1684)
    # data = (
    # maped.lpt, maped.dpt, maped.dpt, maped.len(), maped.den(), p31, p495, maped.p571(), maped.p276(), maped.p195(), maped.p195(),
    # maped.p136(), maped.p170(), maped.p2049(), maped.p2048(), None, None, maped.p186(), maped.p217(),
    # p921, p921, maped.p973(), maped.p5691(), p1684)

    coms = mp.comms(soup)

    """ c_title - títle of image on commons.
        200$a + (BNP + 966$s ) + .jpg
    """
    c_title = "{0} (BNP {1}).jpg".format(coms.u_title(), coms.inv())

    notes = ""
    sk = "<br/>"
    sk+=  coms.c307()

    for i in coms.c304(), coms.c306(), sk:
        if i:

            notes+= i

    refs = ""
    print (coms.c321all())
    for i in coms.c321all():
        if i:
            refs += i
    data = c_title, notes, refs


    return data


def main():
    tdata = list()
    purl_list = "22952", "22953", "22954", "22955", "22956", "22957", "22958", "22959", "22960", "22961", "22962", "22963", "22964", "22965", "22966", "22967", "22968", "22969", "22970", "22971", "22972"

    # purl_list = "22952", "22954"#, "22953", "22954", "22955", "22956", "22957", "22958", "22959"
    # purl_list = "22952"

    for i in purl_list:
        dta = get(i)
        tdata.append(dta)

    print(tdata)
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(tdata)
    #
    # for i in tdata:
    #     print (i)


main()
