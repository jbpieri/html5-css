# Auxiliadores - BREAK
'''
for numero in range(20):
    print(numero)
    # Se o número for = 11, vamos parar o loop
    if numero == 11:
        break
    else:
        print(numero)
'''        
contador = 0

while contador <= 30:
    contador += 1
     
    if contador == 25:
        break
    
    print('O contador esta no valor: ', contador)
   