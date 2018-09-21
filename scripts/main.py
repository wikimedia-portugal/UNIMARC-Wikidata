import requests
from bs4 import BeautifulSoup
from mapper import wd_mapper as mp


url = 'http://urn.bn.pt/purl/unimarc/xml?id=23859&agente=urn.porbase.org'
url_get = requests.get(url)
soup = BeautifulSoup(url_get.content, 'lxml-xml')

maped = mp.endo(soup)
print(maped.lpt)
print (maped.p973)

p31 = "Q3305213"
p921 = ""
p1684 = ""
p495 = "Q45"


print (maped.lpt, ";",maped.dpt, ";",maped.len(), ";",maped.den(), ";",p31, ";",p495, ";",maped.p571(), ";",maped.p276(), ";",maped.p195(), ";",maped.p195(), ";",maped.p136(), ";",maped.p170(), ";",maped.p2049(), ";",maped.p2048(), ";",None, ";",None, ";",maped.p186(), ";",maped.p186(), ";",maped.p217(), ";",p921, ";",p921, ";",maped.p973(), ";",maped.p5691(), ";",p1684)
