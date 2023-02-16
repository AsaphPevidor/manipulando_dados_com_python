# manipulando_dados_com_python

####Bibliotecas e métodos usados no código

Pandas        - Biblioteca usada para manipular dados

Quandl(API)   - Biblioteca utilizada para baixar dados financeiros
              - açoes, taxas de cambio, dados macroenconomicos, commodites...

Matplotlib.pyplo - Biblioteca usada para plotar gráficos

.loc[]    - Método utilizado como filtro utilizado nas linhas(registros)
          - Pode ser usando inclusive para dados temporais

.iloc[]   - Método semelhante ao .loc[]
          - Utiliza coordenadas entre [linha, coluna] para filtrar

.sort()   - Método para ordenação de listas

Manipulação de strings

for in    - Gera loop 

.append() - Método que adiciona items a listas

yfinance  - Biblioteca da Yahoo que possibilita extrair dados do mercado
          - Dados de ações, empresas, dados de mercado em geral (tudo disponivel em bolsas)
          
conjuntos (set) - Coleção em python que possui diversas propriedades que podem ser aplicadas 
                - não permite duplicatas
                
NaN       - Dados faltantes

Wide to long  - Transforma DataFrame comprido(muitas colunas) em um DataFrame mais curto
              Utiliza metodo .melt

Numpy     - Biblioteca que utiliza cálculos da estatística e matemática

.median   - Método da biblioteca numpy, que da o resultado da mediana dos dados

.date_range   - Método do pandas, que permite selecionar as datas através de um intervalo

.str[]    - Método que permite fazer manipulação de dados de uma coluna do DataFrame

.drop     - Método usado para remoção de dados

.count    - Método de contagem

.strftime() - Função que da o dia da semana, a semana que pertence a data

.rename()   - Método que troca nome de colunas ou linhas

.concat()   - Método que junta DataFrames

OHLC        - Formatação de DataFrame (padrão yfinance)

Binning     - Tranforma resultado quantitativo em qualitativo

.crosstab() - Método que cruza informações de 2 colunas no DataFrame

.sort_values  - Método do pandas que ordena coluna do DataFrame

.pivot_table  - 



