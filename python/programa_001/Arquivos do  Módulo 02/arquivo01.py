# Condições ou Condicionais
'''
Nem sempre as linha dos programas serão executadas;

'''
#   Primeira expressão a ser estudada: if

'''
if <condição>:
    bloco se verdadeiro
'''

'''
Identação
O Python  é uma das poucas linguagens de programação que utilizam um recuo, ou deslocamento do texto à direita pra marvar o início eo fim do bloco.

O nome que se dá a esse espaçamento, é IDENTAÇÃO.

Linguagens como Java, C... usa o termo BEGIN, END...

'''

#   Primeiro exemplo: leremos dous valores, e indecaremos qual o maior valor.

primeiroValor = float(input('Digite o primeiro valor): '))
segundoValor = float(input('Digite o segundo valor : '))

if primeiroValor > segundoValor:
    print('O primeiro valor digitado é maior do que o segundo.')

if primeiroValor < segundoValor:
    print('O primeiro valor digitado é menorMENOR do que o segundo.')
    
if primeiroValor == segundoValor:
    print('Os dois valores são iguasis.') 