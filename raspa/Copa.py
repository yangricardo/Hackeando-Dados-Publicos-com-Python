from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.portaltransparencia.gov.br/copa2014/api/rest/empreendimento")
bsObj = BeautifulSoup(html, "xml")
valores = bsObj.findAll('valorTotalPrevisto')

total = 0
for v in valores:
	total = total + float(v.string)
	print(v.string)

print(str(total))