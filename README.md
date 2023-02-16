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

