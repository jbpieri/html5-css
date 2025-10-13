import math

# Função para operações com uma lista.
def descricaoLista(listaNum):
    valorMax = max(listaNum)
    valorMin = min(listaNum)
    somaElem = sum(listaNum)
    media = somaElem / len(listaNum)
    
    resultadosFinais ={
        'Valor Max': valorMax,
        'Valor Min': valorMin,
        'Soma dos Elem': somaElem,
        'Media dos Elem': media
    }
    return resultadosFinais

# print(descricaoLista([1, 5, 8, 10, 50, 120, 1000]))

def mediaArit(num1, num2):
    media = (num1 + num2) / 2
    return media

def circunfInfo(diametro):
    areaCirc = (math.pi) * pow(diametro, 2) /4
    perimCirc = (math.pi) * diametro

    resultadosFinais ={
        'Diametro': diametro,
        'Area': areaCirc,
        'Perimetro': perimCirc
    }
    return resultadosFinais