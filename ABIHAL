import pandas as pd
import requests
from bs4 import BeautifulSoup

hoteis = []
nomes = []
classificações = []
Gerais = []
Endereços = []
CEPs_Cidades = []
Telefones = []
Emails = []
Sites = []
separador = []

p_navegador = requests
link = 'https://abihal.com.br/hoteis'
site = p_navegador.get(link)
#print(f'{site}\n')
html = site.content
soup = BeautifulSoup(html,'html.parser')
conteudo = list(soup.children)[2]
lista_links = soup.find_all('a', href = True)

for a in lista_links:
    hotel = a['href']
    if hotel.startswith('/hoteis/') == True:
        hotel = 'https://abihal.com.br' + hotel
    else:
        hotel = ''
        
    if hotel != '':
            hoteis.append(hotel)
            
del hoteis[0]
        
for i in hoteis:
  p_navegador = requests
  site = p_navegador.get(i)
  html = site.content
  soup = BeautifulSoup(html,'html.parser')
  conteudo = list(soup.children)[3]
  
  nome = soup.find('h3').get_text()
  classificação = soup.find('p',class_= 'lead').get_text()
  geral = soup.find('p',class_= '').get_text() # Precisa ser tratado
  
  separador = []
  organização = geral.split('\n')
  for item in organização:
    while item.startswith(' '):
      item = item[1:]
      item = item
    if item != '':
      separador.append(item)

  endereço = separador[0]
  cep_cidade = separador[1]
  telefone = separador[2]
  email = separador[3]

  nomes.append(nome)
  classificações.append(classificação)
           
  Endereços.append(endereço)
  CEPs_Cidades.append(cep_cidade)
  Telefones.append(telefone)
  Emails.append(email)

  

tabela = pd.DataFrame({'Nome': nomes,
                       'Classificação': classificações,
                       'Endereços': Endereços,
                       'Cep e cidade': CEPs_Cidades,
                       'Telefones':Telefones,
                       'Email':Emails})

tabela

tabela.to_excel('Hoteis Alagoas.xlsx')

