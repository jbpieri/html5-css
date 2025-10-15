# A função range()
'''
range(a, b)

a = inicio do intervalo (sendo o valor incluso)
b = final do intervalo (valor não pertence, não incluso)


'''
from turtle import clear


listaValores= list(range(1, 10))

print(listaValores)



for x in range(1, 10):
    print(x)
    
    
    range(1, 20)
    '''
    range(b) --> range (0, b)
    
    '''
    
print(list(range(20)))

# Criar uma lista que contenha apenas os valores de pares de 0 até 100.

listaComNumPares = []
listaComNumImpares =[]

for num in range(101):
    if(num%2 == 0):
        listaComNumPares.append(num)
    else:
        listaComNumImpares.append(num)
        
print('Lista com pares: ', listaComNumPares)
print()
print('Lista com ímpares: ', listaComNumImpares)

