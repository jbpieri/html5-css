# Estrutura de Repetição = executar um bloc de código repetidamente, obedecento determinadas condições.

# Esstruturas de repetição ou loops.

'''
for
while

'''

# Iniciando pelo for.
# O form é geralmente utilizado para percorrer segueências de dados: listas, por exemplo.
'''

lista = [10, 40, 60, 65, 100]

for item in lista:
    print(item)
    
jogosPlayStation = ['Uncharted', 'God of War', 'BloodBorne', 'FIFA']

for jogo in jogosPlayStation:
    print(jogo)

'''

    
lista = ['Concreto', 'Aço', 6.3, 5, 20, 'Tabela' ]

for elem in lista:
    if type(elem) == str:
        print(elem)
print('-------------')
        
for elem in lista:
    if type(elem) == int:
        print(elem)
        
        
print('-------------')
        
for elem in lista:
    if type(elem) == float:
        print("Encontrei um float!", elem)
        