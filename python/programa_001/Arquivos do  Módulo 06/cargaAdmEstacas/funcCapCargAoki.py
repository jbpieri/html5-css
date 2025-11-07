# import pandas as pd
import math
from tabelasParametros import paramAokiTab, fatorCorrAoki


def searchParamAoki(tipoSolo):
    
    df = paramAokiTab()
    df2 = df.loc[df['Solo'] == tipoSolo]
    listaComK = df2['K (kPa)'].tolist()
    listaComAlfa = df2['Alfa'].tolist()
    
    listaParamAoki = [listaComK[0], listaComAlfa[0]]
    
    return listaParamAoki


def searchCorrAoki(tipoEstaca):
    
    df = fatorCorrAoki()
    df2 = df.loc[df['Tipo de estaca'] == tipoEstaca]
    listaComF1 = df2['F1'].tolist()
    listaComF2 = df2['F2'].tolist()
    
    listaFatorCorr = [listaComF1[0], listaComF2[0]]
    
    return listaFatorCorr


def calc_rpAoki(tipoSolo, tipoEstaca, nspt):
    
    valorK = searchParamAoki(tipoSolo)[0]
    valorF1 = searchCorrAoki(tipoEstaca)[0]
    
    rp = valorK * nspt / valorF1    # rp em kPa
    
    return rp

def calc_rlAoki(tipoSolo, tipoEstaca, nspt):
    
    valorK = searchParamAoki(tipoSolo)[0]
    valorAlfa = searchParamAoki(tipoSolo)[1]
    valorF2 = searchCorrAoki(tipoEstaca)[1]
    
    rl = valorK * nspt * valorAlfa / valorF2
    
    return rl

def propGeomEst(diametro):
    
    perimetroEst = diametro * math.pi
    areaEst = pow(diametro, 2) * math.pi / 4
    
    resultProGeom = [diametro, perimetroEst, areaEst]
    
    return resultProGeom




# testes

# print(searchCorrAoki('Raiz'))
# print(searchParamAoki(1))
# print(calc_rpAoki(12,'HCM',15))
# print(calc_rlAoki(12,'HCM',15))
# print(propGeomEst(0.50))
