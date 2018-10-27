import requests
from bs4 import BeautifulSoup
from mapper import wd_mapper as mp
import csv


def get(purl):
    url = 'http://urn.bn.pt/purl/unimarc/xml?id={}&agente=urn.porbase.org'.format(purl)
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content, 'lxml-xml')

    maped = mp.endo(soup)

    p31 = "Q3305213"
    p921 = ""
    p1684 = ""
    p495 = "Q45"
    p204y = ["", ""]

    # data = (maped.lpt, ";",maped.dpt, ";",maped.len(), ";",maped.den(), ";",p31, ";",p495, ";",maped.p571(), ";",maped.p276(), ";",maped.p195(), ";",maped.p195(), ";",maped.p136(), ";",maped.p170(), ";",maped.p2049(), ";",maped.p2048(), ";",None, ";",None, ";",maped.p186(), ";",maped.p186(), ";",maped.p217(), ";",p921, ";",p921, ";",maped.p973(), ";",maped.p5691(), ";",p1684)
    print("-->", maped.p186(), purl)

    # lpt = str()
    maped.len = '"painting from the BNP collection"'
    qid = None
    # Lpt, Dpt, Lpt - br, Dpt - br, Len, Den
    # maped.lpt = "{}{}{}".format('"',maped.lpt,'"')
    # maped.dpt = "{}{}{}".format('"',maped.dpt,'"')


    data = ( qid,
        maped.lpt, maped.dpt, maped.lpt,maped.dpt, maped.len, maped.den(), p31, p495, maped.p571()[0], maped.p571()[1],
        maped.p571()[2], maped.p571()[3], maped.p571()[4], maped.p276(), maped.p195(), maped.p195(),
        maped.p136(), maped.p170()[0], maped.p170()[1], maped.p2049(), maped.p2048(), maped.p204y()[0],
        maped.p204y()[1], None, None, maped.p186(), maped.p186()[1][0], maped.p186()[1][1], maped.p217(),
        p921, p921, maped.p973(), maped.p5691(), p1684, maped.p195()[0], maped.p195()[1])
    return data


def main():
    tdata = "qid,Lpt,Dpt,Lpt-br,Dpt-br,Len,Den,P31,P495,P571,qal1480,qal1319,qal1326,P276,qal580,P2048,P2049,P2048,qal1012,P2049,qal1012,P136,qal642,P170,qal1773,P793,qal585,P793,qal585,qal642,P793,qal585,P186,P186,qal518,P195,P195,P180,P217,qal195,P5691,P973,P5008"
    purl_list = "22952", "22953", "22954", "22955", "22956", "22957", "22958", "22959", "22960", "22961", "22962", "22963", "22964", "22965", "22966", "22967", "22968", "22969", "22970", "22971"
    purl_list = "22994", "22995", "23001", "23859", "14420", "14421", "22951", "22973", "22974", "22975", "22976", "22977", "22978", "22979", "22980", "22981", "22982", "22983", "22984", "22985", "23009", "23010", "23011", "23012", "23013", "23014", "23015", "23016", "23017", "23018", "26935", "26936", "30865", "22986", "22987", "22988", "22989", "22990", "22991", "22992", "22993", "22996", "22997", "22998", "22999", "23000", "23002", "23003", "23004", "23005", "23006", "23007", "23008"
    # purl_list = "22952", "22953"
    # purl_list = "22994","22995"

    for i in purl_list:
        print(i)
        dta = get(i)
        tdata.append(dta)

    print(tdata)
    with open('wdata.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(tdata)


main()
