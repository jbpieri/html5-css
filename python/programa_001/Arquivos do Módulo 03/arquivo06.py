import numpy as np

primeiroArrayMulti = np.array([[10, 22, 3], 
                               [4000, 5000, 63], 
                               [77, 80, 9]])
'''
Atributos de array

ndarray.ndim        --> número de eixos (dimensões) do array
ndarray.shape       --> uma tupla de inteiros indicando o tamanho do array em cada dimensão
ndarray.size        --> número total de elementos do array
ndarray.dtype       --> tipo dos elementos contidos no array
ndarray.itemsize    --> mostra o tamanho em bytes de cada elemento do array
ndarray.T           --> versão transposta do array

'''

print(primeiroArrayMulti.ndim)

print(primeiroArrayMulti.shape)

print(primeiroArrayMulti.size)

print(primeiroArrayMulti.dtype)

primeiroArrayMulti1 = np.array([[10, 22.2, 3], 
                               [400, 5, 63], 
                               [77, 80, 9]])

print(primeiroArrayMulti1.dtype)

# nao adequado
primeiroArrayMulti2 = np.array([[10, "teste", 3], 
                               [400, 5, 63], 
                               [77, 80, 9]])

print(primeiroArrayMulti2.dtype)


print(primeiroArrayMulti.itemsize)

print(primeiroArrayMulti.T)