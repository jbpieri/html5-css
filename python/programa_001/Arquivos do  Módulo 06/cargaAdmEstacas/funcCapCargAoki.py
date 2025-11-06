# import pandas as pd
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

# testes
# print(searchCorrAoki('Raiz'))
# print(searchParamAoki(1))