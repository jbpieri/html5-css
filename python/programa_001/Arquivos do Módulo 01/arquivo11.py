#   SEQUÊNCIAS
'''
Há tres tipos de sequências nativas em Python.
 
    3) String - str

        - Sequências ordenada de caracteres;
        - Instanciada com caracteres entre aspas simples ou duplas, Ex: 'Cálculo Estrutural!;
        - Os elementos individuais NÃO PODEM SER MODIFICADOS, imutáveis; 

    Os elementos individuais podem ser acessados pelo índice do elemento (sua posição), entre colchetes, após o identificador da sequência.
    O índice dos elementos inicia em 0 e vai até n - 1.=, onde n é o número de elementos.


'''

#   EXEMPLOS DE STRINGS

primeiraString = 'Não é uma string'

print(primeiraString[0])
print(primeiraString[1])
print(primeiraString[2])
print(primeiraString[3])

#   MÉTODO upper()

print(primeiraString.upper())

#   Para mais métodos e funções: https//docs.python.org/3/library/string.html

#   MÉTODO replace()

primeiraString = primeiraString.replace('Não', 'Sim,')
print(primeiraString)

x = 1
x = 10
x = 4000

print(x)

#   função len()

print('O tamanho da string primeiraString é:', len(primeiraString))