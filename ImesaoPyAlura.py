# Importa a biblioteca pandas com o alias 'pd'
import pandas as pd 
# Lê o arquivo Excel 'alura.xlsx' da pasta especificada e carrega os dados da planilha 'Principal' em um DataFrame chamado df_principal
df_principal = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="Principal") 
# Exibe as primeiras 10 linhas do DataFrame df_principal
print(df_principal.head(10))

# Lê o arquivo Excel 'alura.xlsx' da pasta especificada e carrega os dados da planilha 'Total_de_acoes' em um DataFrame chamado df_total_acoes
df_total_acoes = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="Total_de_acoes")
# Exibe o DataFrame df_total_acoes
print(df_total_acoes)

# Lê o arquivo Excel 'alura.xlsx' da pasta especificada e carrega os dados da planilha 'Ticker' em um DataFrame chamado df_Ticker
df_Ticker = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="Ticker")
# Exibe o DataFrame df_Ticker
print(df_Ticker)

# Lê o arquivo Excel 'alura.xlsx' da pasta especificada e carrega os dados da planilha 'ChatGpt' em um DataFrame chamado df_ChatGpt
df_ChatGpt = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="ChatGpt")
# Exibe o DataFrame df_ChatGpt
print(df_ChatGpt)

# Seleciona apenas as colunas 'Ativo', 'Data', 'Último (R$)' e 'Var. Dia (%)' do DataFrame df_principal e cria uma cópia
df_principal = df_principal[['Ativo', 'Data', 'Último (R$)', 'Var. Dia (%)']].copy() 
# Exibe o DataFrame df_principal após a renomeação das colunas
print(df_principal)


# Renomeia as colunas 'Último (R$)' para 'valor_final' e 'Var. Dia (%)' para 'Var_dia_pct' no DataFrame df_principal e cria uma cópia
df_principal = df_principal.rename (columns={"Último (R$)":"valor_final", "Var. Dia (%)":"Var_dia_pct"}).copy()#Nessa linha estamos renomeando a planilha pelo editor de codigo o .copy () faz a modificação
# Exibe o DataFrame df_principal após a seleção das colunas
print(df_principal)

# Calcula a variação percentual dividindo a coluna 'Var_dia_pct' por 100
df_principal['var_pct'] = df_principal['Var_dia_pct'] /100
# Calcula o valor inicial dividindo a coluna 'valor_final' pelo resultado da adição de 1 ao valor da coluna 'var_pct'
df_principal['valor_inicial'] = df_principal['valor_final'] / (df_principal['var_pct'] + 1)
# Exibe o DataFrame resultante
print(df_principal)

# Mescla os DataFrames df_principal e df_total_acoes usando as colunas 'Ativo' e 'Código', respectivamente, como chaves de junção, com junção à esquerda (left join)
df_principal = df_principal.merge(df_total_acoes, left_on='Ativo', right_on='Código', how='left')
# Exibe o DataFrame resultante
print(df_principal)

# Remove a coluna 'Código' do DataFrame df_principal
df_principal = df_principal.drop(columns=['Código'])
# Exibe o DataFrame resultante
print(df_principal)

# Calcula a variação multiplicando a diferença entre 'valor_final' e 'valor_inicial' pelo 'Qtde. Teórica' e atribui o resultado à coluna 'variacao'
df_principal['variacao'] = (df_principal['valor_final'] - df_principal['valor_inicial']) * df_principal['Qtde. Teórica']
# Exibe o DataFrame resultante
print(df_principal)

# Configura a opção de exibição do Pandas para formatar os valores dos DataFrames com duas casas decimais
pd.options.display.float_format = "{:.2f}".format
# Exibe o DataFrame resultante com os valores formatados com duas casas decimais
print(df_principal)

# Converte a coluna 'Qtde. Teórica' para o tipo de dados inteiro (int)
df_principal['Qtde. Teórica'] = df_principal['Qtde. Teórica'].astype(int)
# Exibe o DataFrame resultante
print(df_principal)
# Renomeia a coluna 'Qtde. Teórica' para 'qtd_teorica' no DataFrame df_principal e cria uma cópia
df_principal = df_principal.rename(columns={'Qtde. Teórica': 'qtd_teorica'}).copy() # Nessa linha estamos renomeando a planilha pelo editor de código. O .copy() faz a modificação
# Exibe o DataFrame df_principal após a seleção das colunas
print(df_principal)