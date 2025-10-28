import pandas as pd
import numpy as np
import math

bitolas =[5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0, 32.0]

massa =[]
area =[]

for i in range(len(bitolas)):
    area.append(round((match.pow(bitolas[i],2)* match.pi/400),3))
    massa.append((round((area[i]*0.78),3)))

dicTab={
    'Bitolas (mm)':bitolas,
    'Massa linear (kg/m)':massa,
    'Área de uma barra (cm²)':area
}

taelaAco =pd.DataFrame(dicTab)
print(taelaAco)