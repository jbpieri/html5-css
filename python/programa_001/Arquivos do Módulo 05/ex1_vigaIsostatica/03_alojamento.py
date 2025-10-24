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
    
    condicoes = [2.0, bitola / 10, 1.2 * diamAgreg / 10]
    valorLimite = max(condicoes)
    
    ahSelect = ah[ah >= valorLimite]
    
    # Caractere unicode u03C6 pesquisar
    
    for i in range(len(ahSelect)):
        print(f'{i + 2} \u03C6 {bitola} -> espaçamento = {ahSelect[i]} cm')
    
    return ahSelect

def opcoesAloj(bw, cob, diamEstribo, diamAgreg):
    
    listaBitolas = [5.0, 6.3, 8.0, 10.0, 12.5, 16.0, 20.0, 22.0, 25.0, 32.0, 40.0]
    
    for bitola in listaBitolas:
        
        alojVigas(bw, cob, diamEstribo, diamAgreg, bitola)
    
    return

# EXECUÇÕES

opcoesAloj(20, 3, 5.0, 19)
