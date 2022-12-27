import pandas as pd

sheet = pd.read_excel('hyeondai_autoever.xlsx', sheet_name = '시트1')
col = pd.read_excel('hyeondai_autoever.xlsx', usecols = ['name'])
index_col = pd.read_excel('hyeondai_autoever.xlsx', header=1, index_col=1)
header = pd.read_excel('hyeondai_autoever.xlsx', header=0)

print(index_col)