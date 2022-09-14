# Projeto final
## importando a biblioteca para realizar requisições API
import requests as r
import datetime as dt # para utilização de objetos diferentes que representam tempo
from datetime import date
import csv 

## Url de onde se importa os dados utilizando a biblioteca requests
url = 'https://api.covid19api.com/dayone/country/brazil'
## realizando a requisição e guardando em variavel de resposta
resp = r.get(url)
## checando o código da requisição
# print(resp.status_code)
## guardando os dados que foram retornados pela API em uma variavel chamada RAW_DATA
raw_data = resp.json() # formato utilizado de transmissao de dados pela API
## olhando o que há dentro da variavel
# print(raw_data[0])
# Segunda parte
## Criação de constantes de controle para referenciamento de maneira mais intuitiva
## em relação ao dado que ele representa
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

## Para fins de filtragem de informações necessarias foi criada uma variavel 
final_data = []
for obs in raw_data:
	final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0 , ['confirmados', 'obitos', 'recuperados', 'ativos', 'data'])
## laço FOR com o tamanho da posição 1 até o tamanho da lista
for posicoes in range(1, len(final_data)):
	# sobrescrevendo a posição de data com apenas 10 casas
	final_data[posicoes][DATA] = final_data[posicoes][DATA][:10]

## data escolhida para referenciamento do objeto
## Em 31 de dezembro de 2019, a Organização Mundial da Saúde (OMS) foi alertada sobre
omsAlertada = dt.date(2019, 12, 31)
dataAtual = date.today()
print('Olá \nJá fazem', (dataAtual-omsAlertada).days , 'Dias desde que a Organização Mundial da Saúde (OMS) foi alertada sobre a COVID') #calculo dos dias inclusos no gráfico
# print(dataAtual-omsAlertada).days
## print(dataAtual-omsAlertada).microsecond

## Salvando arquivos de dados
with open('Mundo_covid.csv', 'w') as arquivo:
	writer = csv.writer(arquivo)
	writer.writerows(final_data)

for i in range(1, len(final_data)):
	final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')
## print(final_data) ##objeto ttl



