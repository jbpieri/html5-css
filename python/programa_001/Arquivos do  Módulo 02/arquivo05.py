import math

# Condições ou Condicionais

#   Estruturas aninhadas: colocar um if dentro do outro.

'''
Para escrever m3 digitar alt 0179 no teclado

Uma concreteira chamada engenheirando, tem preços especiais por m³ de concreto usinado forneciso, de acordo com a quantidade solicitada. Obedece a tabela abaixo:

Se a compra for <= 40 m³                                        R$ 300 / m³
Se a compra for maior que 40 m³ e menor ou igual a 80 m³        R$ 270 / m³
Se a compra for maior que 80 m³ e menor do que 120 m³           R$ 240 / m³
Se a compra for maior que 120 m³                                R$ 210 / m³
'''

quantM3Concreto = float(input('Digite a quantidade de Concreto requerida em m³:'))

if quantM3Concreto <= 40:
    precoConcM3 = 300

else:
    
    if quantM3Concreto <= 80:
        precoConcM3  = 270
    else:
        if quantM3Concreto <= 120:
            precoConcM3 = 240
        else:
            precoConcM3 = 210


precoTotal = precoConcM3 * quantM3Concreto

print(f'O valor total da sua compra é R$ {precoTotal} reais, pois o valor por m³ foi R$ {precoConcM3} reais')