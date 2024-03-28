import pandas as pd #quando colocamos as pd estamos dando um apelido para a biblioteca
   
df_principal = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="Principal")
print(df_principal.head(10)) #nesse print especificamos com o Head a quantidade de linhas a sere mostrada
df_total_acoes = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="Total_de_acoes")
print(df_total_acoes)
df_Ticker = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="Ticker")
print(df_Ticker)
df_ChatGpt = pd.read_excel("C:/Ws_Will/Alura/alura.xlsx", sheet_name="ChatGpt")
print(df_ChatGpt)