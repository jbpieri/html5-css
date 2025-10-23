import numpy as np
import math
import pandas as pd


def barrasAco(areaAco):
    
    bitola = np.array([5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 22.0, 25.0, 32.0, 40.0])
    areaBitola = math.pi * pow(bitola / 10, 2) / 4 # dividiu por 10 para passar para cm2
    quantBarras = areaAco / areaBitola
    quantBarrasRound = np.ceil(quantBarras)
    
    exportResult = pd.Series(quantBarrasRound, index=bitola)
    
    return exportResult

print(barrasAco(25))
