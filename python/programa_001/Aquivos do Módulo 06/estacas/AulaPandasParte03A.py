import pandas as pd
import numpy as np

bitolas = [5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0, 32.0]

bit_df = pd.DataFrame(bitolas, columns=['Bitolas (mm)'])

area_bitolas = []
for i in range(len(bitolas)):
    area = np.pi*(bitolas[i]/10)**2/4 #cm²
    area_bitolas.append(area)

massa_bitolas = []
for i in range(len(bitolas)):
    massa_lin = 7850 * np.pi*(bitolas[i]/1000)**2/4 #kg/m
    massa_bitolas.append(massa_lin)
    
#Diametro (mm) | Área de aço (cm²) | Massa linear (kg/m)
tabelaAco = []
for i in range(len(bitolas)):
    tabelaAco.append([bitolas[i],area_bitolas[i],massa_bitolas[i]])
    
tabelaAcoDf = pd.DataFrame(tabelaAco, columns=['Diâmetro (mm)', 'Área (cm²)', 'Massa linear (kg/m)'])

print(tabelaAcoDf)