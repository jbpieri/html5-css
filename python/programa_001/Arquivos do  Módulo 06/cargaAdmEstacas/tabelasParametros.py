import pandas as pd


def paramAokiTab():
    coefKeAlfa = [
        [1, 1000, 0.014],
        [12, 800, 0.020],
        [123, 700, 0.024],
        [13, 600, 0.030],
        [132, 500, 0.028],
        [2, 400, 0.030],
        [21, 550, 0.022],
        [213, 450, 0.028],
        [23, 230, 0.034],
        [231, 450, 0.030],
        [3, 200, 0.060],
        [31, 350, 0.024],
        [312, 300, 0.028],
        [32, 220, 0.040],
        [321, 330, 0.030]
        
    ]
    
    dfParamAoki = pd.DataFrame(coefKeAlfa, columns=['Solo', 'K (kPa)', 'Alfa'])
    
    
    return dfParamAoki


def fatorCorrAoki():
    
    corrAoki = [
        ['Escavada', 3.0, 6],
        ['Raiz', 2.0, 4],
        ['HCM', 2.0, 4]
    ]       
    
    dfCorrecaoAoki = pd.DataFrame(corrAoki, columns=['Tipo de estaca', 'F1', 'F2'])
      
    return dfCorrecaoAoki
