#%%
import pandas as pd
import numpy as np

#%%
dclientes = pd.read_excel("../dados/dClientes.xlsx")
dclientes.head()

#%%
dcategorias = pd.read_excel("../dados/dCategorias.xlsx")
dcategorias.head()

#%%
dcategorias.info()

#%%
dcategorias = dcategorias.astype({"id_DRE": "Int64"})

#%%
dcategorias.head()

#%%
dcategorias[dcategorias["id_DRE"] == 11]
#%%
fcontas_receber = pd.read_excel("../dados/fContasReceber.xlsx")
fcontas_receber.head()

#%%
fcontas_receber[fcontas_receber["CodCategoria"] == 101]

#%%
fcontas_receber['DataPagamento'] = pd.to_datetime(fcontas_receber['DataPagamento'], errors='coerce')

#%%
df_receber_completo = fcontas_receber.merge(dcategorias, left_on='CodCategoria', right_on='id_Categoria_Nivel_3', how='left') 
df_receber_completo.head()
#%%
faturamento_por_categoria_ano = df_receber_completo.groupby('id_Categoria_Nivel_3')['Valor'].sum().sort_values(ascending=False)
faturamento_por_categoria_ano

#%%
faturamento_por_categoria_ano = df_receber_completo.groupby('Categoria_Nivel_3')['Valor'].sum().sort_values(ascending=False)
faturamento_por_categoria_ano
#%%
principal_categoria = faturamento_por_categoria_ano.index[0]
valor_principal_categoria = faturamento_por_categoria_ano.iloc[0]

resultado_anual = f"A categoria de receita que mais vendeu no ano foi '{principal_categoria}', com um faturamento de R$ {valor_principal_categoria:,.2f}."
print(resultado_anual)

#%%
df_receber_completo
#%%
vendas_janeiro = df_receber_completo[df_receber_completo['DataPagamento'].dt.month == 1]
# vendas_janeiro = df_receber_completo[(df_receber_completo['DataPagamento'].dt.month >= 4) & (df_receber_completo['DataPagamento'].dt.month <= 6)]
vendas_janeiro

#%%
faturameto_janeiro = vendas_janeiro["Valor"].sum()
faturameto_janeiro