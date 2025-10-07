import math

# Condições ou Condicionais

#   Segunda expressão a ser estudada: else

'''
else:
    bloco se o if passado form Falso
'''


#   Programa que calculaa o ec2 e o ecu para um fck recebido do usuário.
#   Receber dados do usuário (calor do fck)

fck = float(input('Insira o valor do fck (MPa) '))

#   Cálculo do ec2 e ecu

if fck <= 50:
    ec2 = 2 / 1000
    ecu = 3.5 /1000

else:
    ec2 = (2 / 1000) + ((0.085 / 1000) * (math.pow(fck - 50, 0.53)))
    ecu = (2.6 / 1000) + ((35 / 1000) * (math.pow((90 - fck)/ 100, 4)))
    
print(f'O concreto que você esta utilizando , tem fck de {fck} MPa')
print(f'O valor do ec2 para este caso, é {ec2 * 1000} por mil. O valor de ecu para este caso, é {ecu * 1000} por mil')
