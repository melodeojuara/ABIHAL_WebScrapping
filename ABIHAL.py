import pandas as pd
import requests
from bs4 import BeautifulSoup

def teste_igualdade(var1,var2,m_sucesso,m_falha):
  print('Testando resposta do sistema...')
  if var1 == var2:
    resposta = 1
    print(m_sucesso)
  else:
    resposta = 0
    print(m_falha)

  return resposta

NOMES = []
CLASS = []
TELEF = []
EMAIL = []
SITES = []
RUAS_ = []
NUMER = []
CIDAD = []
CEP__ = []

#Realizando teste de conexão
resposta = 0
while resposta == 0:
  site = p_navegador.get('https://abihal.com.br/hoteis')
  resposta = teste_igualdade(str(site), '<Response [200]>','Conexão realizada', 'Conexão Falhou')

# Selecionando links disponíveis no site e limpando ruído
html = site.content
soup = BeautifulSoup(html,'html.parser')
conteudo = list(soup.children)[3]
lista_links = soup.find_all('a', href = True)

hoteis = []
for a in lista_links:
    hotel = a['href']
    if hotel.startswith('/hoteis/') == True:
        hotel = 'https://abihal.com.br' + hotel
    else:
        hotel = ''
        
    if hotel != '':
            hoteis.append(hotel)

del hoteis[0]

# Entrando nos links individualmente        
for i in hoteis:
  p_navegador = requests
  site = p_navegador.get(i)
  html = site.content
  soup = BeautifulSoup(html,'html.parser')
  conteudo = list(soup.children)[3]

  geral = [i.get_text() for i in soup.find_all('h3', {"class":"nott ls0 fw-semibold"})]
  endereco = geral[0].split(',')

  NOMES.append(soup.find("li", {"class": "breadcrumb-item active"}).get_text())
  CLASS.append(soup.find("span", {"class": "before-heading text-secondary"}).get_text())
  TELEF.append(geral[1])
  EMAIL.append(geral[2])
  SITES.append(geral[3])
  RUAS_.append(endereco[0])
  NUMER.append(endereco[1])
  CIDAD.append(endereco[2])

  try:
    CEP__.append(endereco[3])
  except:
    CEP__.append('Not Found')

tabela = pd.DataFrame({'Nome': NOMES,
                       'Classificação': CLASS,
                       'Telefone': TELEF,
                       'E-mail': EMAIL,
                       'Site': SITES,
                       'Rua': RUAS_,
                       'Número': NUMER,
                       'CIDADE': CIDAD,
                       'CEP': CEP__})

tabela.to_excel('Hoteis Alagoas.xlsx')
