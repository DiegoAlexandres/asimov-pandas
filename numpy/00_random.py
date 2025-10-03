#%%
import pandas as pd
import numpy as np

#%%
df = pd.DataFrame(
    np.random.randn(5, 5),
    columns =['A', 'B', 'C', 'D', 'E'],
    index=['Linha1', 'Linha2', 'Linha3', 'Linha4', 'Linha5']
)
df

#%%
df_positivo = pd.DataFrame(
    np.random.rand(5, 5),
    columns =['Q', 'W', 'E', 'E', 'R'],
)

df_positivo

#%%
df_interiro = pd.DataFrame(
    np.random.randint(1, 101, size=(5, 5)),
    columns =['Z', 'X', 'C', 'V', 'B'],
)

df_interiro

#%%
df.iloc[2:3, [1, 2]] = np.nan
df

#%%
df.iloc[2: 3, 1: 2] = np.nan   
df