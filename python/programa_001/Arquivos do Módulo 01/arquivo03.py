#Variáveis


# São símbolos com identificadores associados a valores/literais guardados na memória.

x = 42

print (x)
print (type (x))
FraseTeste = 'A inteligencia artificisl é uma excelente ferramento para otimização de estrutura de concreto armado.'
FraseTeste2 = 'Mas, não consegue substituir o engenheiro estrutural.'


#   1) Nomear utilizando um identificador contenso: caracteres em minúsculo, maiúsculo, undercore _
#   2) Atribuir o valor usando o operador =
#   3) Podemos utilizar digitos, mas nunca como primeiro caractere do identificador.

# Exemplo
# 3y = 5 --> não pode ser uma variável porque começa com digito
y3 = 32


divteste = x / y3


print (y3)
print (FraseTeste, FraseTeste2)
print (FraseTeste + FraseTeste2)
print (x + y3)
print (divteste)
print (type(divteste))

#   PALAVRAS RESERVADAS NO PYTHON
#   False, true, if, not, and, None, Global, try
#   False = 4  : NÃO UTILIZAR

# BOAS PRÁTICAS PARA VARIÁVEIS

#   1) Elas precisam ser claras.
fck = 30    # variável bem clara

#   2) usar minúsculas e maiúsculas. (sem exagerar no tamanho do nome)
tensaoDeCalculo = 2.64

#   3) usar o underscore _

tensao_de_calculo = 2.64