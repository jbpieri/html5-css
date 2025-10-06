#   Entrada de dados (inputs)
#   A função input() sempre recebe valores do tipo String, ou seja, nã importa se digitamos um float, int ou str.

baseDaViga = float(input('Digite o valor da base da sua viga (m): '))
alturaDaViga = float(input('Digite o valor da altura da sua viga (m): '))
comprimentoTotalDaViga = float(input('Digite o comprimento total da sua viga (m): '))

#   Cálculo do volume de concreto

volumeViga = (baseDaViga) * (alturaDaViga) * (comprimentoTotalDaViga)

#   Representar para o usuário os resultados finais

print(f'A sua viga tem as siguintes dimensões: {baseDaViga} m de base, {alturaDaViga} m de altura, {comprimentoTotalDaViga} m de comprimento total.')
print(f'Portando, o volume de concreto da viga é {volumeViga} m3.')

#   ERROS COMUNS:
'''
1) Tentar fazer operações matemáticas com strings. Ou seja, esquecer de converter os valores em float ou int.

'''



