from urllib.request import urlopen
from bs4 import BeautifulSoup
def extrai_salário(id_s):
    url = 'http://www.portaldatransparencia.gov.br/servidores/Servidor-DetalhaRemuneracao.asp?Op=2&IdServidor=%s&CodOrgao=26238&CodOS=15000&bInformacaoFinanceira=True' %id_s
    html = urlopen(url)
    s = BeautifulSoup(html.read(), 'html.parser')
    if 'Total da Remuneração Após Deduções' not in str(s):
        return 0
    x = s.findAll('tr', {'class':'remuneracaodetalhe'})
    valor = x[2].find('td', {'class':'colunaValor'})
    valor = valor.string.replace('.', '')
    valor = valor.replace(',', '.')
    return valor

for p in range(1, 1002):
    print ('-------Página', p)
    u = 'http://www.portaldatransparencia.gov.br/servidores/OrgaoLotacao-ListaServidores.asp?CodOS=15000&DescOS=MINISTERIO%20DA%20EDUCACAO&CodOrg=26245&DescOrg=UNIVERSIDADE%20FEDERAL%20DO%20RIO%20DE%20JANEIRO&Pagina=' + str(p)
    html = urlopen(u)
    s = BeautifulSoup(html.read(), 'html.parser')
    tabelas = s.findAll('table')
    funcs = tabelas[1].findAll('tr')
    funcs = funcs[1:]

    arq = open('ufrj2.txt', 'a')
    for f in funcs:
        dados = f.find('a')
        h = dados['href']
        j = h.find('=') + 1
        k = h.find('&')
        id_s = h[j:k]
        arq.write (h[j:k] + ',')
        arq.write(dados.string.strip()+',')
        sal = extrai_salário(id_s)
        print (sal)
        arq.write(str(sal))
        arq.write('\n')
    arq.close()