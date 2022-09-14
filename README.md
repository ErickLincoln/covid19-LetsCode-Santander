# Projeto final Letscode e Santander

## Finalidade
Contruir um projeto compilando todo o conhecimento adquirido durante o curso para criação de aplicação única.

## Sobre a criação:
Projeto de pesquisa de dados com utilização de API pública

### Dos dados:
Os dados de COVID19 do Brasil colhidos da API escolhida estão incompletos, mas nada que impossibilite a criação do projeto.

Primeira parte:

## importação de dados utilizando a biblioteca requests
    -Importando a biblioteca para realizar requisições API para utilização de objetos diferentes que representam tempo.
    - Realizando a requisição e guardando em variavel de resposta.
    - Checando o código da requisição.
    - Guardando os dados que foram retornados pela API em uma variavel.

# Segunda parte:
## Constantes de controle:
    - Criação de constantes de controle para referenciamento de maneira mais intuitiva em relação ao dado que ele representa.
    - Filtragem de informações necessarias foi criada uma variavel com laço FOR com o tamanho da posição 1 até o tamanho da lista.
    - Sobrescrevendo a posição de data com apenas 10 casas e com a data escolhida para referenciamento do objeto "Em 31 de dezembro de 2019" data em que  a Organização Mundial da Saúde (OMS) foi alertada sobre a Covid.
    - Salvando arquivos de dados do objeto ttl em csv.

# Principais funções da aplicação
## Função de visualização dos resultados criados:
    - Responsavel pela chave que constrói os dados reais em Y.
    - Recepção dos dados reais de Y, com Y podendo conter um ou mais dados
    - Recepção de lista com o 'labels de Y(identificção)' de cada um destes dados de Y.
    -Checagem se Y é tipo lista ou um valor comum.
    - Y = lista - Inicialização de variavel "datasets" como lista com os valores de Y e o label respectivo de cada.
### exploração das listas 'y' e 'labels':
    - Criação de 'datasets':
        - dicionário com as chaves => 'label' e 'data'
    - Finalização do laço for, com retorno da lista 'datasets':
        - caso o y nao seja uma lista de listas, preciso retornar uma lista que contém um unico valor de dicionário que tem um label que idealmente é a lista de label mas com um unico valor de posição 0, mais y que é um unio valor.

## Função de definição de título
    - Chamada como 'set_title' 
    - Função para recepção do titulo(title) de fato.
    - valor padrão = 'vazio'.
    
## Função que gera o dicionário de representação gráfica
    - Manipulação de todos os valores referentes ao gráfico.
    - Variaveis de recepção: ##  'dataset' e 'options'.
    - Dicionário representante do gráfico.
    - Dicionário com setup de informações: 'titulo', 'identificação de eixos' e retorno do fim da função com dicionário representativo de gráficos.

## Função de requisição de API utilizando dicionário 'chart'
    - Recepção do dicionário
    - função com objetivo de realizar requisição e retornar o valor binário em 'content' para armazenamento.
    - Acesso de API com requisição e valores guardados em 'variavel de resposta'.
    - Chamada de retorno de arquivo de imagem.
    - retorno do valor binário para: entendimento, compreensão e armazenamento da imagem em máquina.
## Função responsável pelo salvamento da imagem
    - manipulação de path de salvamento.
    - manipulação de 'content'(conteudo do arquivo binário 'wb' de valor).

## Função de visualização dos resultados criados
    Dados escolhidos:
    - Confirmados
    - Recuperados
    - Obitos
    Ajuste de valores de manipulação: 
    - Dados finais
    - Datas
    - Dados finais na posição de data.
# covid19-LetsCode-Santander
