#   SEQUÊNCIAS
'''
Há tres tipos de sequências nativas em Python.
 
    1) Lista - list

        - Sequências mutáveis, ordenadas de elementos de qualquer tipo, incluindo outra sequência;
        - Instanciada com valores entre colchetes, separados por vírgula. ex: [4,1,20];
        - Os elementos da lista, PODEM SER MODIFICADOS, ADICIONADOS, REMOVIDOS, ETC; 

    Métodos e funções importantes para listas:

    appende()  - Inclusão de elementos na lista.
    del        - Excluir elementos.

'''

#   EXEMPLOS DE LISTAS

primeiraLista =['String dentro da lista!', 25, 4.67, [7, 9, 10], (1, 7, 8)]

print(primeiraLista)
print(primeiraLista[0])
print(primeiraLista[1])
print(primeiraLista[2])
print(primeiraLista[3])
print(primeiraLista[4])
print(primeiraLista[3][2])

# A lista é mutável... veja:

primeiraLista[1] = 2000
print(primeiraLista[1])

# MÉTODO APPEND()

listaDeBitolas = []

# Inserindo elementos em uma lista após ela ter sido criada.

listaDeBitolas.append(5.0)
listaDeBitolas.append(6.3)
listaDeBitolas.append(8.0)
listaDeBitolas.append(10.0)
listaDeBitolas.append(12.5)
listaDeBitolas.append(16.0)
listaDeBitolas.append(20.0)
listaDeBitolas.append(25.0)

# Método insert()

listaDeBitolas.insert(7, 22.0)

print(listaDeBitolas)

# Função del()

del(listaDeBitolas[7])

print(listaDeBitolas)

