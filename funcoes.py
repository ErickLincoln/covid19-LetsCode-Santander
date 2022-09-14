# Principais funções da aplicação
# Função de visualização dos resultados criados
from main import *
from PIL import Image
from IPython.display import display
from urllib.parse import quote
## responsavel pela chave que constrói os dados reais de Y
### pra isso recebo os dados reais de Y, com Y podendo conter um ou mais dados
### e lista com o 'labels de Y(identificção)' de cada um destes dados de Y
def get_datasets(y, labels):
    if type(y[0]) == list: # verifico o tipo do primeiro valor que é passado pra Y é tipo lista ou um valor comum
        datasets = [] # caso seja uma lista vou inicializar uma variavel "datasets" que será uma lista com os valores de Y e o label respectivo de cada um
        for i in range(len(y)): # exploramos aqui ambas as listas 'y' e 'labels'
          datasets.append({ # crio aqui dentro da lista 'datasets' um dicionário contendo
            'label' : labels[i], # um dicionário que contem a 'chave => label' que sera a 'lista de labels => labels', na 'posição atual => [i]
            'data' : y[i] # e a 'chave => data' que contém o Y na posição atual
          })
        return datasets 
    else: # finalização do laço for, com retorno da lista'datasets'
        # caso o y nao seja uma lista de listas, preciso retornar uma lista que contém
        #  um unico valor de dicionário que tem um label que idealmente é a lista de label
        #  mas com um unico valor de posição 0, mais y que é um unio valor
        return [{
            'label': labels[0], 
            'data': y
        }
        ]
# função de definição de título 
def set_title(title=''): # chamada como 'set_title' que só recebe o titulo(title) de fato, valor padrão vazio
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return { #retorna um simples dicionário com a chave=>contendo titulo, com mais uma chave dizendo se o titulo será mostrado
        'title': title,
        'display': display # se valor de titulo for diferente de string vazia
    }

# criação de função que gera o dicionário de representação gráfica
    ## recebe todos os valores referentes ao gráfico
    ##  no corpo 'dataset' e 'options' são variaveis de recepção
def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)

    chart = { # dicionário que representa o gráfico
        'type': kind,
        'data': { # também é um dicionário
            'labels': x,
            'datasets': datasets
        },
        'options': options # finalizando o dicionário com setup de informações de titulo e identificação de eixos
    }

    return chart # retorno do fim da função com dicionário representativo de gráficos

    ## Função de requisição de API utilizando dicionário 'chart'
    ### para recepção do dicionário
    ### O objetivo da função é fazer requisição e retornar o valor binário 'content' para armazenamento
def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart' # Acesso de API
    resp = r.get(f'{url_base}?c={str(chart)}') # requisição pra API e guardando em 'variavel de resposta' 
        #chamada responsavel por retornar o arquivo de imagem 
    return resp.content # retorna a partir da função o valor binário para: entender, compreender e armazenar a imagem na maquina

# Função responsável pelo salvamento da imagem
## path = caminho de save
## content = conteudo do arquivo binário
def save_image(path, content):
    with open(path, 'wb') as image:#wb de valor binario
        image.write(content)

# Função de visualização dos resultados criados
def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in final_data[1::45]: # parti da posição 1 pra evitar o Header, plotando de 45 em 45 dias 
	y_data_1.append(obs[CONFIRMADOS]) #jogando os valores de confirmados 

y_data_2 = []
for obs in final_data[1::45]: #parti da posição 1 pra evitar o Header, plotando de 45 em 45 dias 
	y_data_2.append(obs[ATIVOS]) #jogando os valores de Ativos

y_data_3 = []
for obs in final_data[1::45]: # parti da posição 1 pra evitar o Header, plotando de 45 em 45 dias 
	y_data_3.append(obs[OBITOS]) # jogando os valores de Obitos 

labels = ['Confirmados', 'Ativos', 'Obitos']

x =[] # valores de manipulação: dados finais e datas
for obs in final_data[1::45]:
	x.append(obs[DATA].strftime('%d-%m-%Y')) # dados finais na posição de data

chart = create_chart(x, [y_data_1, y_data_2, y_data_3], labels, title='Gráfico confirmados vs Ativos vs Obitos')
chart_content = get_api_chart(chart)
save_image('semestral.png', chart_content)
display_image('semestral.png')

def get_api_qrcode(link):
    text = quote(link)
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')