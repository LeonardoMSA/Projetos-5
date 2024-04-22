import pandas as pd

# Carregando o dataset
df = pd.read_csv('./restaurantes.csv')

columns_to_remove = ['telefone', 'email', 'site']

# Removendo as colunas do DataFrame
df = df.drop(columns=columns_to_remove)

df.to_csv('restaurantes1.csv', index=False)