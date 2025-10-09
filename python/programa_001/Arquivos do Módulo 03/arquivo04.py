# Numpy

# https://numpy.org/doc/1.25/user/absolute_beginners.html

import numpy as np

# Numpy Arrays

'''
Estrutura de dados, em que todo elemnto deve ser so mesmo tipo. Geralmente float ou int;
Mais eficientes que as listas do Python;
Cada dimensão do array é chamado de eixo (axis);
Os eixos são numeros a partir de 0;
Acessados utilizando colchetes [];

'''

lista = [1, 3, 5, 7, 9]

primeiroArray = np.array(lista)
segundoArray = np.array([10, 20, 50, 20, 12])

print(primeiroArray)
print(segundoArray)
print(type(primeiroArray))
print(type(lista))

arrayComZeros = np.zeros((10))
print(arrayComZeros)

arrayComUm = np.ones((15))
print(arrayComUm)

primeiroArange = np.arange(0, 11, 2)
print(primeiroArange)

primeiroArange1 = np.arange(0, 11, 0.001)
print(primeiroArange1)

quantElem = np.size(primeiroArange1)
print(quantElem)