import math

def calcAreaAço_mm_cm2(bitola):
    
    areaDeAco = math.pi * pow(bitola / 10, 2) / 4
    
    return areaDeAco


listaComBitolas = [5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 25.0]
listaComAreaAco = []

for bitola in listaComBitolas:
    listaComAreaAco.append(calcAreaAço_mm_cm2(bitola))
    
print(listaComAreaAco)