# -*- coding: utf-8 -*-
"""DS - 03. Manipulação de Dados com Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ik9E7je_joW1dLcrf-KGQ_bwKpfL6IZZ

Manipulação de Dados com Python

O objetivo deste módulo é dar início ao processo de transformação e processamento de dados, para deixar no formato que precisamos antes de realizar a análise. Além disso, mostraremos como filtrar, modificar e juntar diferentes tipos de dados.

# 1. Bibliotecas

Dando continuidade ao que aprendemos no módulo anterior, neste módulo continuaremos explorando todo o potencial da biblioteca pandas.

Esta é a biblioteca de referência que devemos usar quando há necessidade de processamento e tratamento de dados.

Além disso, vamos mostrar alguns procedimentos que podemos realizar com dados, utilizando para isso dados financeiros como exemplo.
"""

# Execute apenas se for preciso instalar as bibliotecas

!pip install pandas, numpy
!pip install datetime
!pip install matplotlib plotly
!pip install yfinance quandl

# Manipulação de dados
import pandas as pd
import numpy as np

# Visualização de dados
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Importação de dados financeiros
import yfinance as yf
import quandl

"""# 2. Criar e organizar um dataframe

## 2.1. Dataframe simples, uma coluna

Vamos utilizar a API da Quandl (Nasdaq) que já vimos anteriormente para fazer a extração dos dados da Selic.
"""

# Aqui você deve inserir sua senha de acesso da API

quandl.ApiConfig.api_key = "4NFLzs3fgqxK3JHsN-dX"

# Os códigos referentes a cada papel / moeda / taxa de juros podem ser obtidos na busca do proprio site da Quandl
# Nesse caso, a selic é representada por BCB/432

selic = quandl.get("BCB/432", start_date="2000-01-01",end_date="2022-12-31")

plt.figure(figsize=(10,10))
plt.plot(selic)
plt.show()

# Vamos inspecionar o formato dos dados

selic.head()

"""Observe a estrutura do data frame acima. Perceba que ele possui apenas uma coluna e um índice (data). Data frames assim são fáceis de trabalhar pois as tarefas realizadas nele são automaticamente aplicadas a sua única coluna, portanto não é necessário mencionar o nome desta única coluna.

Os dataframes lembram muito os nossos conhecidos arquivos de planilha como Excel ou Google Sheets

## 2.2. Filtros simples

Imagine que você trabalha num banco e agora lhe foi dada a tarefa de selecionar um valor de Selic para um dia específico. Como você poderia fazer?

É para resolver problemas assim que existem os métodos .loc e .iloc. Como eles funcionam?

A ideia desses métodos é de possibilitar um filtro nos nossos dados para obter uma linha ou célula específicas.

##### O método .loc

O .loc é utilizado quando o filtro deve ser feito com a métrica utilizada no índice do nosso dataframe.

Por exemplo, a métrica utilizada como índice no nosso dataframe é data. Portanto, nesse caso devemos usar o .loc com a data que queremos fazer o filtro.

Imagine que o seu gestor te perguntou qual era o valor da Selic no dia 26/05/21

Você poderia ter feito assim:
"""

selic_filtrada = selic.loc['2021-05-26']
selic_filtrada

# Para obter os dados entre duas datas específicas

selic_filtrada = selic.loc['2019-03-26':'2021-05-26']
selic_filtrada.plot()

# Filtrando a partir de uma data específica e indo até o último dia disponível

selic_filtrada = selic.loc['2019-03-26':]
selic_filtrada.plot()

# Obtendo os dados desde o início e indo até uma data limite específica, nesse caso 26/03/2017

selic_filtrada = selic.loc[:'2017-03-26']
selic_filtrada.plot()

"""##### O método .iloc

O .iloc é utilizado quando o filtro deve ser feito com a posição da linha dentro do nosso dataframe.

Por exemplo, caso você precise da linha 0 ou linha 1. Ou mesmo se precisar da linha 200 até a linha 500.

Exemplos:
"""

# Obtendo a linha 0 (primeira linha, excluindo o cabeçalho)

selic_filtrada = selic.iloc[0]
selic_filtrada

# Obtendo a linha 1 (lembrar sempre da indexação iniciando em 0 no Python)

selic_filtrada = selic.iloc[1]
selic_filtrada

# Obtendo a linha 200

selic_filtrada = selic.iloc[200]
selic_filtrada

# Obtendo a última linha

selic_filtrada = selic.iloc[-1]
selic_filtrada

# Obtendo da linha 20 até a linha 200 (lembrando também da indexação, 200 não inclusiva)

selic_filtrada = selic.iloc[20:200]
selic_filtrada.plot()

# Obtendo todas as linhas até a linha 100 (linha 100 não entra)

selic_filtrada = selic.iloc[:100]
selic_filtrada.plot()

"""## 2.3. Noções importantes de dataframes

Para demonstrar manipulações de dados em um dataframe de várias colunas, vamos extrair os dados das ações que compõem o IBOV

Para saber a composição atualizada do IBOV, acesse o link:
https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm

Nesta seção, vamos utilizar algumas bibliotecas de dados de mercado financeiro, como a yfinance, que extrai dados do Yahoo Finance

Os ativos que compõem o IBOV são os seguintes:


['WEGE3', 'EMBR3', 'AZUL4', 'CCRO3', 'ECOR3', 'GOLL4', 'RAIL3', 'POSI3', 'BRFS3', 'JBSS3', 'MRFG3', 'BEEF3', 'ABEV3', 'ASAI3', 'CRFB3', 'PCAR3', 'NTCO3', 'AMER3', 'SOMA3', 'LREN3', 'MGLU3', 'PETZ3', 'VIIA3', 'ALPA4', 'CYRE3', 'EZTC3', 'JHSF3', 'MRVE3', 'CVCB3', 'COGN3', 'RENT3', 'LCAM3', 'YDUQ3', 'BRML3', 'IGTI11', 'MULT3', 'BIDI11', 'BPAN4', 'BBDC3', 'BBDC4', 'BBAS3', 'BPAC11', 'ITSA4', 'ITUB4', 'SANB11', 'BBSE3', 'IRBR3', 'SULA11', 'B3SA3', 'CIEL3', 'DXCO3', 'KLBN11', 'SUZB3', 'BRAP4', 'CMIN3', 'VALE3', 'BRKM5', 'GGBR4', 'GOAU4', 'CSNA3', 'USIM5', 'RRRP3', 'CSAN3', 'PETR3', 'PETR4', 'PRIO3', 'UGPA3', 'VBBR3', 'HYPE3', 'RADL3', 'FLRY3', 'HAPV3', 'GNDI3', 'QUAL3', 'RDOR3', 'LWSA3', 'CASH3', 'TOTS3', 'VIVT3', 'TIMS3', 'SBSP3', 'CMIG4', 'CPLE6', 'CPFE3', 'ELET3', 'ELET6', 'ENBR3', 'ENGI11', 'ENEV3', 'EGIE3', 'EQTL3', 'TAEE11']

Vamos transformar isso agora numa lista
"""

tickers_IBOV = ['WEGE3', 'EMBR3', 'AZUL4', 'CCRO3', 'ECOR3', 'GOLL4', 'RAIL3', 'POSI3', 'BRFS3', 'JBSS3', 'MRFG3', 'BEEF3', 'ABEV3', 'ASAI3', 'CRFB3', 'PCAR3', 'NTCO3', 'AMER3', 'SOMA3', 'LREN3', 'MGLU3', 'PETZ3', 'VIIA3', 'ALPA4', 'CYRE3', 'EZTC3', 'JHSF3', 'MRVE3', 'CVCB3', 'COGN3', 'RENT3', 'LCAM3', 'YDUQ3', 'BRML3', 'IGTI11', 'MULT3', 'BIDI11', 'BPAN4', 'BBDC3', 'BBDC4', 'BBAS3', 'BPAC11', 'ITSA4', 'ITUB4', 'SANB11', 'BBSE3', 'IRBR3', 'SULA11', 'B3SA3', 'CIEL3', 'DXCO3', 'KLBN11', 'SUZB3', 'BRAP4', 'CMIN3', 'VALE3', 'BRKM5', 'GGBR4', 'GOAU4', 'CSNA3', 'USIM5', 'RRRP3', 'CSAN3', 'PETR3', 'PETR4', 'PRIO3', 'UGPA3', 'VBBR3', 'HYPE3', 'RADL3', 'FLRY3', 'HAPV3', 'GNDI3', 'QUAL3', 'RDOR3', 'LWSA3', 'CASH3', 'TOTS3', 'VIVT3', 'TIMS3', 'SBSP3', 'CMIG4', 'CPLE6', 'CPFE3', 'ELET3', 'ELET6', 'ENBR3', 'ENGI11', 'ENEV3', 'EGIE3', 'EQTL3', 'TAEE11']

# Como ordenar esses papéis em ordem alfabética?

tickers_IBOV.sort()
tickers_IBOV

"""**PONTO IMPORTANTE**

As ações brasileiras no Yahoo Finance terminam com ".SA". Isso é válido inclusive para outros papéis, como ETFs, FIIs, BDRs

Como acrescentar ".SA" ao fim do nome de um papel?

Veja o raciocínio abaixo:
"""

acao = 'PETR4'

acao + ".SA"

# Observe que "somamos" o ".SA" ao ticker de "PETR4"

"""Precisamos então criar uma estrutura que faça isso para todos os papéis de uma vez"""

ativo_SA = 0
tickers_IBOV_SA = []

for i in tickers_IBOV:
  ativo_SA = (i+'.SA')
  tickers_IBOV_SA.append(ativo_SA)

tickers_IBOV_SA

"""Uma vez que temos uma lista com o nome dos tickers corrigidos para fazer a busca na yfinance (que extrai os dados da Yahoo Finance)"""

# Extração para um ativo

yf.download("PETR4.SA", start='2022-02-01', end='2022-02-18', period = "1d")

"""Observe a estrutura dos dados acima. Temos Abertura, Máxima, Mínima, Fechamento, Fechamento Ajustado e Volume. Podemos reproduzir a mesma estrutura caso queiramos obter dados de vários papéis ao mesmo tempo."""

# Na yfinance as vezes pode ocorrer erros na busca de alguns ativos (usualmente se for uma unit). Note que nesse caso houve um erro em BIDI11
# Pode ver que é um problema pontual https://finance.yahoo.com/quote/BIDI11.SA/history?p=BIDI11.SA

yf.download(tickers_IBOV_SA, start='2022-02-10', end='2022-02-18', period = "1d")

"""Perceba que a estrutura acima replica as 5 colunas (Abertura, Máxima, Mínima, Fechamento, Fechamento Ajustado e Volume) para todos os papéis. Isso cria uma estrutura muito grande e difícil de trabalhar. É melhor selecionar apenas uma coluna específica para esses papéis:"""

# Nesse caso, estamos não apenas extraindo os dados, mas armazenando na variável cotacoes_IBOV

cotacoes_IBOV = yf.download(tickers_IBOV_SA, start='2022-02-10', end='2022-02-18', period = "1d")

"""
Para facilitar nossa vida, podemos obter apenas os dados da coluna **Adj Close** para todos os papéis de uma vez"""

yf.download(tickers_IBOV_SA, start='2022-02-10', end='2022-02-18', period = "1d")['Adj Close']

"""Perceba que reduzimos o número de colunas de 552 para 92 (Adj Close dos 92 ativos da lista)

Vamos criar um novo dataframe com o resultado da busca de cotação ao longo de todo o período de 2021, considerando todos as colunas disponíveis (OHLC, Adj Close e Volume)
"""

cotacoes_IBOV = yf.download(tickers_IBOV_SA, start='2021-01-01', end='2021-12-31', period = "1d")

# Reforçando a complexidade do dateframe, composto por pois índices de colunas
# Indice 0 para os parâmetros das cotações e índice 1 para os ativos

cotacoes_IBOV.columns

# Usando o set (conjunto) podemos remover as duplicatas e ver a lista de parâmetros disponíveis

set(cotacoes_IBOV.columns.get_level_values(0))

# Filtrar apenas o índice que contém os preços de Adj Close

cotacoes_IBOV_Adj_Close = cotacoes_IBOV['Adj Close']
cotacoes_IBOV_Adj_Close

# Filtrar apenas o índice que contém os preços de Adj Close e ABEV3.SA ao mesmo tempo (acaba sendo uma única coluna)
# Como é apenas uma coluna, ele desconsidera o formato dateframe e traz como um formato "series" da biblioteca pandas
# Usando pd.DataFrame podemos reconfigurar como dataframe

cotacoes_IBOV_Adj_Close_ABEV3 = cotacoes_IBOV[('Adj Close','ABEV3.SA')]
cotacoes_IBOV_Adj_Close_ABEV3 = pd.DataFrame(cotacoes_IBOV_Adj_Close_ABEV3)
cotacoes_IBOV_Adj_Close_ABEV3

"""## 2.4. Manejo dos NAs e NaN"""

# O método isna() retorna um booleano (True/False). Como vimos, no Python o True equivale a 1 e False equivale a 0.
# Se eu somar uma coluna/linha composta por True/False eu consigo saber qts True existem (e nesse caso do .isna, saber qts NAs existem)
# O método sum() = sum(0), já que 0 é o default do método e representa a soma de todos as células de uma coluna. Se colocarmos sum(1), teremos a soma de todas as celulas de uma linha

count_null = cotacoes_IBOV.isna().sum()
count_null

# O output a seguir me mostra que existe 1 NA na coluna de Adj Close de ABEV3 (podemos checar a data logo abaixo pra ver pq isso aconteceu com todos os ativos)
# Já ASAI3 possui 38 células com NA. Começou a ser negociada no IBOV em março apenas

# Soma dos NAs por linhas. Primeira linha 18 NAs. Lembrando que uma linha é composta por 6 índices 0 (Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume), podemos concluir que existem 3 ativos (18/6) com NA na primeira linha

count_null_linha = cotacoes_IBOV.isna().sum(1)
count_null_linha

# O método shape retorna o número de linhas e coluna de um dataframe

cotacoes_IBOV.shape

# Duas formas de obter o número de colunas

print(cotacoes_IBOV.shape[1])
len(cotacoes_IBOV.columns)

# Usando as informações do shape e do isna, podemos fazer um filtro para retornar quais linhas (cotacoes_IBOV.shape[0]) ou colunas cotacoes_IBOV.shape[1] possuem uma fração específica de NAs
# No exemplo, exibir as linhas onde temos pelo menos 1 NA

cotacoes_IBOV[cotacoes_IBOV.isna().sum(1)>0]

# Agora um filtro de NA mais complexo, onde os NAs representem mais de 50% dos dados de uma linha (NAs da linha/total de colunas > 0.5).
# Vemos que nenhuma linha possui tantos NAs

cotacoes_IBOV[(cotacoes_IBOV.isna().sum(1)/len(cotacoes_IBOV.columns))>0.5]

# Vemos que retornou os dados de uma data onde não houve pregão

# Sabendo disso, posso usar o dropna para retirar qq linha que seja NA para o ativo ABEV3
# Usando o argumento inplace nem preciso criar uma nova variável (ex., cotacoes_IBOV2 que represente dados sem os NAs da sexta-feira de Pascoa)

cotacoes_IBOV.dropna(subset = [('Adj Close', 'ABEV3.SA')], inplace=True)

# Maioria dos ativos contém todos os dados de cotações

count_null = cotacoes_IBOV.isna().sum()
count_null

# Assim conseguimos saber quais ativos possuem pelo menos 1 NA

cotacoes_IBOV.columns[cotacoes_IBOV.isna().sum()>=1]

# Posso remover qualquer coluna (ativo) que apresente algum NA usando drop. Esse método exige um argumento (axis) informando se a remoção deve ocorrer nas linhas ou colunas. Axis = 1 colunas
# Note que ASAI3 por ex nao aparece mais no dataframe

cotacoes_IBOV_filter_NA = cotacoes_IBOV.drop(cotacoes_IBOV.columns[cotacoes_IBOV.isna().sum()>=1], axis=1)
cotacoes_IBOV_filter_NA.columns

# Nesse caso, vemos que não há nenhum NA na tabela

count_null = cotacoes_IBOV_filter_NA.isna().sum()
max(count_null)

# ASAI3 por exemplo nao está mais neste dataframe

cotacoes_IBOV_filter_NA

"""## 2.5. Redução do número de colunas - "Wide to Long" """

# Vamos aproveitar esse dataframe sem nenhum NA e trabalhar em cima dele.
# Neste caso, vamos apenas criar uma cópia dele, deixando-o com um nome um pouco mais simples

cotacoes_ativos = cotacoes_IBOV_filter_NA

cotacoes_ativos

"""#### Método melt

O melt é utilizado na biblioteca pandas para realizar uma transformação que chamamos de "wide to long".

Ou seja, se tivermos um dataframe grande e largo podemos transformá-lo num dataframe longo, com poucas colunas mas com muitas linhas.

O que antes eram as colunas agora viram categorias em colunas novas, as "variáveis", e os valores são todos mostrados na coluna valor, ou "value".


"""

# Veja que a quantidade de dados é a mesma, porém agora temos apenas 3 colunas e o índice (contendo as datas). Em contrapartida, passamos a ter mais de 130 mil linhas
# Essa estrutura é especialmente interessante para trabalharmos com filtros, análises estatísticas e modelagens em geral

cotacoes_ativos_long = pd.melt(cotacoes_ativos,ignore_index=False)
cotacoes_ativos_long

# Exibindo o nome das colunas

cotacoes_ativos_long.columns

"""## 2.6. Renomeando colunas"""

# Usamos um dicionário para renomear as colunas, contendo a estrutura {'nome antigo' : 'novo nome'}

cotacoes_ativos_long = cotacoes_ativos_long.rename({'variable_0':'Parametro', 
                                                    'variable_1':'Ativo', 'value':'Valor'}, axis=1)
cotacoes_ativos_long

# Categorias presentes na coluna "Parametro" (sem repetição)

set(cotacoes_ativos_long['Parametro'])

# Categorias presentes na coluna "Ativo" (sem repetição)

set(cotacoes_ativos_long['Ativo'])

"""## 2.7. Filtros e substituições"""

# Vamos criar uma cópia do dataframe original para fazermos algumas práticas de filtros e substituições

df_cotacoes = cotacoes_ativos_long.copy()
df_cotacoes

# Vamos filtrar o dataframe selecionando apenas as linhas onde a coluna "Parametro" possui a categoria "Adj Close"

df_cotacoes_Adj_Close = df_cotacoes[df_cotacoes.Parametro == 'Adj Close']
df_cotacoes_Adj_Close

# mesmo filtro feito de outra forma

df_cotacoes_Adj_Close = df_cotacoes[df_cotacoes['Parametro'] == 'Adj Close']
df_cotacoes_Adj_Close

# Filtros com mais de uma condição

# Além de filtrar a coluna "Parametro", agora queremos estabelecer um filtro também na coluna "Valor"
# queremos selecionar as linhas que possuem valor menor de 10
# Por causa da presença do "&", as duas condições precisam ser respeitadas

df_cotacoes_Adj_Close_low_cost = df_cotacoes[(df_cotacoes.Parametro == 'Adj Close') & (df_cotacoes.Valor < 10)]
df_cotacoes_Adj_Close_low_cost

# Selecionando apenas as linhas que possuem dados de Volume
df_cotacoes_Volume = df_cotacoes[df_cotacoes.Parametro == 'Volume']

df_cotacoes_Volume

# Calculando a mediana do valor de Volume de todos os papéis
volume_mediano = np.median(df_cotacoes_Volume.Valor)
volume_mediano

# Vamos selecionar apenas os pregões onde o volume negociado por ativo foi acima da mediana de volume calculada acima
df_cotacoes[(df_cotacoes.Valor > volume_mediano)]

# Vamos complicar um pouco mais
# Além do filtro acima, vamos criar um outro filtro onde a coluna Parametro precisa ser "Adj Close" e o valor precisa ser menor que 10 OU maior que 80

df_cotacoes[(df_cotacoes.Parametro == 'Adj Close') & ((df_cotacoes.Valor < 10) | (df_cotacoes.Valor > 80))]

# Vamos selecionar ativos com base em uma lista
# Ou seja, precisamos filtrar as linhas de tal forma que contenham apenas os papéis que determinamos na lista

ativos_churrasco = ['ABEV3.SA','JBSS3.SA','CRFB3.SA','KLBN11.SA','RADL3.SA']
df_cotacoes_churrasco = df_cotacoes[df_cotacoes.Ativo.isin(ativos_churrasco)]
df_cotacoes_churrasco

# Como selecionar todos os papéis que não estão na lista?

alguns_bancos = ['ITUB4.SA','BBDC4.SA','BBAS3.SA','SANB11.SA','BIDI11.SA',]
df_cotacoes_nao_bancos = df_cotacoes[~df_cotacoes.Ativo.isin(alguns_bancos)]
df_cotacoes_nao_bancos

# Vamos lembrar como funciona o .loc

df_cotacoes_index = df_cotacoes.loc['2021-03-26']
df_cotacoes_index

# Utilizando o operador "date_range" para retornar todas as datas que estão presentes em um intervalo

data_range_IBOV = pd.date_range(start='2021-03-21',end='2021-03-31')
data_range_IBOV

# Utilizando o elemento construído na célula anterior, vamos selecionar as linhas do nosso data frame de ativos que contém apenas
# o intervalo de datas determinado acima

df_cotacoes_index_range = df_cotacoes[df_cotacoes.index.isin(data_range_IBOV)]
df_cotacoes_index_range

# Lembrando dos operadores de filtros em strings, veja como fazemos para retornar o quinto caractere do ticker de um papel

acao = 'PETR4.SA'
acao[-4]

"""Dado isso, como podemos fazer para retornar apenas as ações ordinárias, ou seja, que têm final '3'?"""

# Realizando o mesmo filtro acima, só que para toda a coluna "Ativo", que contém os tickers dos papéis

df_cotacoes.Ativo.str[-4]

# Dado o que aprendemos acima, basta então criar uma condição lógica de tal forma que "df_cotacoes.Ativo.str[-4]" seja igual a "3"
# Nessa caso, temos todos os dados desses ativos

df_cotacoes_ordinarias = df_cotacoes[df_cotacoes.Ativo.str[-4]=='3']
df_cotacoes_ordinarias

# E agora, uma lista de ações preferenciais

set(df_cotacoes_ordinarias['Ativo'])

# Para remover os ".SA" dos tickers, precisamos usar um método chamado "replace"
# Precisamos indicar o que queremos remover e o que virá no lugar
# r'.SA$' nos indica qualquer palavra terminada em .SA

df_cotacoes_semSA = df_cotacoes.replace(to_replace=r'.SA$', value='',regex=True)
df_cotacoes_semSA

# Para trocar "VIIA" por "VVAR", o raciocínio é o mesmo:
# Nesse caso, ^ para indicar uma string que comece com VIIA

df_cotacoes_ativo_alterado = df_cotacoes.replace(to_replace=r'^VIIA', value='VVAR',regex=True)
set(df_cotacoes_ativo_alterado.Ativo)

df_cotacoes_semSA.head()

"""## 2.8. Duplicatas"""

# Análise de duplicatas
df_cotacoes_semSA.duplicated().any()

"""Ou seja, então há duplicatas. Vamos fazer uma verificação mais precisa coluna a coluna"""

print(df_cotacoes_semSA['Parametro'].duplicated().any(),
df_cotacoes_semSA['Ativo'].duplicated().any(),
df_cotacoes_semSA['Valor'].duplicated().any())

df_cotacoes_semSA[df_cotacoes_semSA.duplicated(keep=False)]

df_cotacoes_semSA.shape

# Caso quiséssemos remover as duplicatas

sem_duplicatas = df_cotacoes_semSA.drop_duplicates(subset=['Parametro', 'Ativo','Valor'], keep=False)
sem_duplicatas.shape

sem_duplicatas.head()

"""## 2.9. Drop

Trata-se da função que deve ser utilizada quando precisamos remover linhas ou colunas
"""

sem_duplicatas.index

pd.to_datetime('2021-01-04')

# Suponha que você quer remover duas datas:

a = pd.to_datetime('2021-01-04')
b = pd.to_datetime('2021-01-05')
c = pd.to_datetime('2021-01-06')

sem_duplicatas.drop([a,b,c])

# Observe acima que as datas escolhidas sumiram do dataframe

# Podemos também remover colunas, pelo nome:
sem_duplicatas.drop(['Valor'], axis = 1)

# Podemos remover pelo índice
sem_duplicatas.drop(sem_duplicatas.columns[[0,1]], axis = 1)

"""# 3. Consolidação de dataframes

Veremos nessa seção alguns métodos e ferramentas para criar novos dataframes com base em dataframes pré-existentes

Essas operações vão nos possibilitar condensar os dataframes originais em novos de tal forma que consigamos reter a maior parte das informações relevantes

Exemplos:
1. count
2. concat
3. group by
4. merge (join)

## 3.1. count

Conta células que não são NAs para cada linha ou coluna.

Lembre-se sempre de consultar a documentação oficial da biblioteca e da função em caso de dúvida.
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html
"""

df_cotacoes_semSA.count(axis=0)

df_cotacoes_semSA.count(axis=1)

"""## 3.2. Concatenar outros DFs e reorganizar colunas"""

IBOV_shares = df_cotacoes_semSA.copy()
IBOV_shares.head()

tickers_futuros_IBOV = ['^BVSP']
##### cotacoes_IBOV = yf.download(tickers_IBOV_SA, start='2021-01-01', end='2021-12-31', period = "1d")

Dia_semana = pd.to_datetime(IBOV_shares.index).strftime('%A')
Dia_semana

# Inserir o dia da semana como uma nova coluna no dataframe
IBOV_shares.insert(0, 'Dia_semana', Dia_semana)
IBOV_shares.head()

# Ajustando formatação do mês e transformando num novo dataframe
Mes = pd.DataFrame(pd.to_datetime(IBOV_shares.index).strftime('%B'))

# Mudando nome da coluna
Mes = Mes.rename({'Date':'Mes'},axis=1)

# Ajustando o índice para que seja o mesmo do dataframe IBOV_shares, ou seja, o índice passará a ser a data
Mes.index = IBOV_shares.index
Mes

# Ajustando formatação do ano e transformando num novo dataframe
Ano = pd.DataFrame(pd.to_datetime(IBOV_shares.index).strftime('%Y'))

# Mudando nome da coluna
Ano = Ano.rename({'Date':'Ano'},axis=1)

# Ajustando o índice para que seja o mesmo do dataframe IBOV_shares, ou seja, o índice passará a ser a data
Ano.index = IBOV_shares.index

Ano

# Vamos então utilizar o método concat para juntar Mes e Ano num novo dataframe:

ibov_data = pd.concat([Mes,Ano],axis=1)

ibov_data.head()

# Agora juntando com o dataframe original com os dados dos papéis
IBOV_shares_datas = pd.concat([IBOV_shares,ibov_data],axis=1)
IBOV_shares_datas.head()

# Vamos mudar a ordem das colunas

# Determine a nova ordem que deseja
col_nova_ordem = ['Ano','Mes','Dia_semana','Parametro','Ativo','Valor']
IBOV_shares_datas = IBOV_shares_datas[col_nova_ordem]
IBOV_shares_datas.head()

set(IBOV_shares_datas.Parametro)

"""### Reconstrução do dataframe

Utilizando o conhecimento que adquirimos até aqui sobre formatação de data frames e junção usando a função concat, vamos tentar recuperar a formatação que tínhamos nos dados das ações antes de executar o melt.
Antes disso, tínhamos a estrutura OHLC
"""

# Inicialmente vamos criar novos dataframes, de tal forma que cada informação de negociação será um data frame separado.
# por exemplo, teremos um data frame para dados de abertura (Open), máxima, mínimia, etc.

IBOV_Open = IBOV_shares_datas[IBOV_shares_datas.Parametro == 'Open']
IBOV_High = IBOV_shares_datas[IBOV_shares_datas.Parametro == 'High']
IBOV_Low = IBOV_shares_datas[IBOV_shares_datas.Parametro == 'Low']
IBOV_Close = IBOV_shares_datas[IBOV_shares_datas.Parametro == 'Close']
IBOV_Adj_Close = IBOV_shares_datas[IBOV_shares_datas.Parametro == 'Adj Close']
IBOV_Volume = IBOV_shares_datas[IBOV_shares_datas.Parametro == 'Volume']

# Exemplo
IBOV_Open.head()

# Renomeado as colunas "Value" de cada um dos dataframes para que faça mais sentido, e não cause problemas quando juntarmos todos eles
# OBS.: O Warning não siginifica erro.

IBOV_Open.rename(columns={'Valor':'Open'},inplace=True)
IBOV_High.rename(columns={'Valor':'High'},inplace=True)
IBOV_Low.rename(columns={'Valor':'Low'},inplace=True)
IBOV_Close.rename(columns={'Valor':'Close'},inplace=True)
IBOV_Adj_Close.rename(columns={'Valor':'Adj Close'},inplace=True)
IBOV_Volume.rename(columns={'Valor':'Volume'},inplace=True)

# Removendo colunas desnecessárias

IBOV_Open.drop('Parametro',axis=1)

# Precisamos do inplace = True para que as mudanças façam efeito
# OBS.: O Warning não siginifica erro.
IBOV_Open.drop(['Parametro'],axis=1, inplace = True)

IBOV_Open.head()

# OBS.: O Warning não siginifica erro.
IBOV_High.drop(IBOV_High.columns[0:5],axis=1, inplace = True)

IBOV_High.head()

# Outra forma de fazer o filtro
IBOV_Close[IBOV_Close.columns[4:6]]

IBOV_shares_ohlc = pd.concat([IBOV_Open,IBOV_High,IBOV_Low.drop(IBOV_Low.columns[0:5],axis=1),
                              IBOV_Close[IBOV_Close.columns[5:6]],IBOV_Adj_Close[IBOV_Adj_Close.columns[5:6]],IBOV_Volume[IBOV_Volume.columns[5:6]]],
                              axis=1)
IBOV_shares_ohlc

"""## 3.3. Binning

Realizamos essa operação quando precisamos criar variáveis qualitativas que representam as categorias de uma variável numérica anterior.

Para realizar a operação de binning, vamos criar algumas colunas novas.
"""

IBOV_shares_ohlc.head()

# Criação de coluna que indica o retorno nominal (em R$) no preço da ação após o pregão

IBOV_shares_ohlc['Resultado_oc'] = (IBOV_shares_ohlc['Close']-IBOV_shares_ohlc['Open'])/(IBOV_shares_ohlc['Close'])
IBOV_shares_ohlc.head()

"""Binning manual

Criação de uma coluna que diz se o resultado dia foi positivo ou negativo:
"""

Resultado_oc = IBOV_shares_ohlc['Close']-IBOV_shares_ohlc['Open']
Resultado_bin = []

for i in Resultado_oc:
  if i > 0:
    Resultado_bin.append('Positivo')
  else:
    Resultado_bin.append('Negativo')

IBOV_shares_ohlc['Result_bin'] = Resultado_bin
IBOV_shares_ohlc.head()

"""## 3.4. Crosstab

Criação uma nova tabela cruzada de frequência com base em informações solicitadas.

No exemplo abaixo, estamos obtendo a frequência de pregões negativos e positivos para cada um dos meses presentes no nosso dataframe.
"""

crosstab_meses = pd.crosstab(IBOV_shares_ohlc['Mes'],IBOV_shares_ohlc['Result_bin'])
crosstab_meses

"""Vamos criar algumas colunas auxiliares para demonstrar em termos percentuais a ocorrência de pregões positivos ou negativos."""

crosstab_meses['Total']=crosstab_meses.Negativo+crosstab_meses.Positivo
crosstab_meses['Neg_%']=crosstab_meses.Negativo/crosstab_meses.Total*100
crosstab_meses['Pos_%']=crosstab_meses.Positivo/crosstab_meses.Total*100
crosstab_meses.sort_values('Pos_%',ascending=True)

"""## 3.5. Pivot table

Uma tabela que agrupa itens individuais (ou categorias) de uma tabela maior  em uma ou mais características (variáveis) da tabela. 

Essas sumarização pode ocorrer usando soma, média ou outras medidas estatísticas. 

Na tabela abaixo, por exemplo, estamos consolidando a média do resultado diário dos pregões (retorno) para cada um dos meses.
"""

pivot_table_meses = pd.pivot_table(IBOV_shares_ohlc, values="Resultado_oc", 
                                   index=["Mes"], columns=[],aggfunc=np.mean)
pivot_table_meses.sort_values('Resultado_oc',ascending=True)

"""Criando uma nova pivot table, desta vez com as medianas:"""

pivot_table_meses = pd.pivot_table(IBOV_shares_ohlc, values="Resultado_oc", index=["Mes"], columns=[],aggfunc=np.median)
pivot_table_meses.sort_values('Resultado_oc',ascending=True)

"""## 3.6. Group by

Método para agrupar um dataframe usando como base uma ou mais variáveis.

Esta operação envolve a seleção de uma ou mais variáveis como referência para o agrupamento e uma função de consolidação para calcular o resultado.
"""

IBOV_shares_ohlc.head()

# Resultado médio agrupado por ativo

IBOV_shares_ohlc.groupby(['Ativo']).mean()

# Valores médios de Open, High, Low, Close, Adj Close, Volume e resultado diário para os papéis, por mês
IBOV_shares_ohlc.groupby(['Ativo', 'Mes']).mean()

# Na média, qual o resultado por mês de Weg com relação ao retorno intraday?

IBOV_shares_ohlc[IBOV_shares_ohlc['Ativo']=='WEGE3'].groupby(['Ativo', 
                                                              'Mes']).mean().sort_values(by = 'Resultado_oc')

"""Observe que de acordo com a tabela acima, os melhores meses para WEGE3 são julho, janeiro e setembro.

E com relação a dias da semana?
"""

IBOV_shares_ohlc[IBOV_shares_ohlc['Ativo']=='WEGE3'].groupby(['Ativo', 'Dia_semana']).mean().sort_values(by = 'Resultado_oc')

"""Qual foi o volume total negociado de WEGE3 ao longo dos anos e meses?"""

IBOV_shares_ohlc[IBOV_shares_ohlc['Ativo']=='WEGE3'].groupby(['Ano','Mes']).sum().sort_values(by = 'Volume')

"""Houve uma tendência de redução do volume negociado de WEGE3 ao longo do ano!

Qual dos papéis foi mais negociado?
"""

IBOV_shares_ohlc.groupby(['Ativo']).sum().sort_values(by = 'Volume')

# Transformando em dataframe para visualização

volumes = IBOV_shares_ohlc.groupby(['Ativo']).sum().sort_values(by = 'Volume')

import matplotlib.pyplot as plt

y = volumes.Volume

x = volumes.index

# Initialize a Figure and an Axes
fig, ax = plt.subplots()

# Fig size
fig.set_size_inches(12,20)

# Create horizontal bars
ax.barh(y=volumes.index, width=volumes.Volume);

"""## 3.7. Join (ou merge)

Operação realizada para unir dois dataframes diferentes.

Estes dataframes podem ou não conter dados para os mesmos indivíduos, observações  ou datas, por isso é necessário especificar qual tipo de join vamos aplicar.
"""

!pip install Image

from IPython.display import Image

# Abrindo imagens
Image(filename = 'Tipos_de_join.jpg', width=700, height=450)

"""### 3.7.1. Abrindo uma nova tabela"""

import pandas as pd
import yfinance as yf

ibov = pd.read_csv('Bovespa.csv')

ibov.head()

ibov.WEGE3.plot()

"""Vamos extrair dados de outras fontes"""

lren = yf.download('LREN3.SA', start = '2017-01-01', end = '2021-07-20')

lren.head()

lren.Close.plot()

"""Modificar os nomes das colunas de adjusted close"""

lren.rename(columns = {'Adj Close': 'LREN3'}, inplace = True)

lren.head()

"""Filtrando coluna específica no data frame de IBOV"""

acao = 'BBAS3'
ibov.index = pd.to_datetime(ibov.Date)
BBAS = ibov[acao]

BBAS.head()

BBAS.plot()

novo = pd.merge(BBAS, lren, how = 'inner', on = 'Date')

novo.head()

cotacoes = novo[['BBAS3','LREN3']]

cotacoes.head()

cotacoes.head()

cotacoes.plot();

petro = IBOV_shares_ohlc[IBOV_shares_ohlc['Ativo']=='PETR4']
petro.rename(columns={'Adj Close':'PETR4'}, inplace = True)
petro.head()

petro.columns

final = pd.merge(novo, petro, how = 'inner', on = 'Date')

final.shape

"""Por que o join não retornou nenhuma linha? Porque não há interseção dos dados!"""

final = pd.merge(novo, petro, how = 'outer', on = 'Date')

final.shape

final.head()

final[['BBAS3','LREN3','PETR4']].plot()

"""### Perceba então o resultado: temos dados para períodos diferentes em cada um dos papéis!

É exatamente por isso que o gráfico resultante acima ficou com um "vazio".

"""

