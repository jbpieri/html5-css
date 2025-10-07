#   SEQUÊNCIAS
'''
Há tres tipos de sequências nativas em Python.
 
    1) Tupla - tuple

        - Sequência ordenada de elementos de qualquer tipo, incluindo outra siquência qualquer;
        - Instanciada com valores entre parênteses, separados por vírgula. ex: (4,1,20);
        - Aplicação mais comum: em registros, ou guardar termos que não serão MODIFICADOS;
        - Os elementos da tupla, NÃO PODEM SER MODIFICADOS; 

        ex: fck disponíveis em um programa... (20, 25, 30, 35, 40, 45, 50)

'''

#   EXEMPLOS DE TUPLAS

primeiraTupla = (14, 'Essa é uma String!', 6.75, (2, 7, 8))

    # os valores dos elementos podem ser acessados utilizando o índice do elemento entre colchetes.
    # lembrando que, no Python, o primeiro elemento de uma sequência é o elemento de índice 0.
    # As sequências iniciam no elemento 0 e vão até o elemento n - 1, onde n é o número de elementos na sequência.

# Primeiro elemento da Tupla:

print(primeiraTupla[0])
print(primeiraTupla[1])
print(primeiraTupla[2])
print(primeiraTupla[3])

# O valor na posição 3, é uma tupla, portanto, podemos "aninhar " sequências.

print(primeiraTupla[3][1]) 

# ERROS TÍPICOS

'''
- Tentar alterar os elementos dentro da Tupla;
    ex: primeiraTupla[1] = 1.6

    - Acessar elementos que não existem na Tupla; 
    ex: print(primeiraTupla[4])

'''