# Funções

# Funções nativas do Python...

# len() - fornece o tamanho de uma lista, array, etc por exemplo

a = [1, 2, 4, 6, 8]

print(a)

print(len(a))
print('')
# função sum() -- soma todos os elementos de uma lista etc.

a = [3, 5, 7]
print(sum(a))
print('')

# função type() -- indica o tipo de variável.

a = [3, 5, 7]
print(type(a))
print('')

# função input() -- recebe um dado do usuário.
'''
a = float(input('Digite o valor da base da sua viga (m): ')) 
print(a)
print('')
'''


# Podemos programar as nossas próprias funções...
'''
def <identificador da função>(parâmetros da função):
    <código identado parte da função>
    return: ...
    
    o return é no caso da função retornar alguma coisa.

'''

# Criar uma função que fornece o valor da média aritmética de dois números.

def mediaArit(num1, num2):
    media = (num1 + num2) / 2

    return media

print(mediaArit(10,30))
