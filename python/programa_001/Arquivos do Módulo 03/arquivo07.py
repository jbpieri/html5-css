import numpy as np

primeiroArrayMulti = np.array([[10, 16, 3], 
                               [40, 5, 63], 
                               [74, 80, 9]])

# mostra a primeira linha com os 3 valores
print('Imprime a primeira linha')
print(primeiroArrayMulti[0])
print('Imprime a segunda linha')
print(primeiroArrayMulti[1])
print('Imprime a terceira linha')
print(primeiroArrayMulti[2])

print('Imprime um único elemento da matriz, neste caso o [0, 0] imprime 10')
print(primeiroArrayMulti[0, 0])

print('Imprime um único elemento da matriz, neste caso o [1, 1] imprime 5')
print(primeiroArrayMulti[1, 1])

'''
Operações com as matrizes

'''
arrayParaOperx = np.array([4, 7, 12, 87, 100, 108, 45])

# Somar todos os elementos do array

print(arrayParaOperx.sum())



arrayMulti1 = np.array([[10, 16, 3], 
                        [40, 5, 63], 
                        [74, 80, 9]])

arrayMulti2 = np.array([[0,    14, 1000], 
                        [56,    2,   59], 
                        [243, 123,   87]])


# Multiplicar a matriz 1 com a 2 --> vai gerar uma terceira matriz (array) com os valores multiplicados

arrayResultMult1 = arrayMulti1 * arrayMulti2 # multiplicação dos elementos das matrizes

print(arrayResultMult1)
print('')
# para fazer multiplicação entre as matrizes utilizamos .dot

arrayResultMult2 = arrayMulti1.dot(arrayMulti2)

print(arrayResultMult2)
print('')

# soma os valores das linhas da matriz = 300
print(arrayMulti1.sum())

# soma os valores somente das colunas da matriz = [124 101  75]
print(arrayMulti1.sum(axis = 0))

# soma os valores somente das linhas da matriz = [ 29 108 163]
print(arrayMulti1.sum(axis = 1))


# determinante do array utiliza np.linalg que são as funções de algebra
print('')
print(np.linalg.det(arrayMulti1))
print('')
print(np.linalg.det(arrayMulti2))
print('')




# para achar o valor mínimo de um array
print('')
print(arrayParaOperx.min())
print('')

print('')
print(arrayMulti2.min())
print('')


# para achar o valor máximo de um array
print('')
print(arrayParaOperx.max())
print('')

# para achar a média de um array
print('')
print(arrayMulti1.mean())
print('')


# para achar a variancia dos elementos de um array
print('')
print(arrayMulti1.var())
print('')


# para achar o desvio padrão dos elementos de um array
print('')
print(arrayMulti2.std())
print('')