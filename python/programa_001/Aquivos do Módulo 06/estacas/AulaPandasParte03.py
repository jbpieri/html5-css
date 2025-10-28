import pandas as pd
import numpy as np


dicTabelaAco = {
    'Bitolas (mm)': [5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0],
    'Massa linear (kg/m)': [0.16, 0.25, 0.40, 0.63, 1.0, 1.6, 2.5, 4.0],
    'Áre de uma barra (cm²)': [0.20, 0.315, 0.50, 0.80, 1.25, 2.0, 3.15, 5.0]
}

tabelaAcoDF2 = pd.DataFrame(dicTabelaAco)

# Selecionando colunas
print(tabelaAcoDF2[['Bitolas (mm)', 'Massa linear (kg/m)']])

# Selecionando linhas
print(tabelaAcoDF2.loc[0])


