bitolaAco = float(input("Insira a bitola de aço em (mm): "))
QuantDeBitola = float(input('Insira a quantidade de bitola: '))

bitolaAco = bitolaAco /10 

#if bitolaAco == 5.0 or bitolaAco == 6.3 or bitolaAco == 8.0 or bitolaAco == 10.0 or bitolaAco == 12.5 or bitolaAco == 16.0 :

AreaDeAcoTotal = (3.1415 * (bitolaAco ** 2)) / 4 * QuantDeBitola


print(AreaDeAcoTotal)