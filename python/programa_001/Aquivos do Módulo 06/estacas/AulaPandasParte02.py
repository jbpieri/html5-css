import pandas as pd
import numpy as np

'''
O panda trabalha como se fosse, ou de forma parecida com uma tabela de excel.
DataFrame = colunas, linhas e dados nesses elementos.
'''

# Criando dataframe por meio de listas

bitolas = [5.0,
           6.3,
           8.0,
           10.0,
           12.5,
           16.0,
           20.0,
           25.0]

dfBitolas = pd.DataFrame(bitolas, columns=['Bitolas (mm)'])

# print(dfBitolas)
# Bitola / massa linear kg/m / Área de aço de uma barra
linhasDoDF = [[5.0, 0.16, 0.20], 
              [6.3, 0.25, 0.315],
              [8.0, 0.40, 0.50],
              [10.0, 0.63, 0.80],
              [12.5, 1.0, 1.25],
              [16.0, 1.6, 2.0],
              [20.0, 2.5, 3.15],
              [25.0, 4.0, 5.0]]


tabelaAcoDF = pd.DataFrame(linhasDoDF, columns=['Bitolas (mm)', 'Massa linear (kg/m)', 'Áre de uma barra (cm²)'])

# Criando dataframe por meio de discionários

dicTabelaAco = {
    'Bitolas (mm)': [5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0],
    'Massa linear (kg/m)': [0.16, 0.25, 0.40, 0.63, 1.0, 1.6, 2.5, 4.0],
    'Áre de uma barra (cm²)': [0.20, 0.315, 0.50, 0.80, 1.25, 2.0, 3.15, 5.0]
}

tabelaAcoDF2 = pd.DataFrame(dicTabelaAco)

print(tabelaAcoDF2)

