import numpy as np



def alojVigas(bw, cob, diamEstribo, diamAgreg, bitola):
    
    # bw (cm)
    # cob (cm)
    # diaEstribo (mm)
    # diaAgreg (mm)
    # bitola (mm)
    
    dispAloj = bw - (2 * cob) - (2 * diamEstribo / 10)
    
    
    quantBarras = np.linspace(2, 100, 99)
    
    ah = (dispAloj - (quantBarras * bitola / 10)) / (quantBarras - 1)
    
    
    return ah

print(alojVigas(20, 3, 5.0, 19, 10.0))

