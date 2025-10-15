# while - utilizar quando queremos que um bloco de código seja executado ENQUANTO alguma condição estiver sendo satisfeita.

'''
while <condição>:
    <bloco executado>
'''

'''
Sobre a condição

1) Verificar o valor de uma cariável...
2) Verificar o valor do retorno de uma função...
3) Se uma estrutura de dados se igualar a um determinado número de elementos...

Para interronper um programa, use ctrl + c (mesmo comando de copiar do windows)

'''

y = 1

while y <= 20:
    print(y)
    y = y + 1
    
print()

contador = 0

while contador <= 30:
    print('O contador esta no valor: ', contador)
    contador = contador + 1