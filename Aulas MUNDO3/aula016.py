lanche = ('Hambúguer', 'Esfiha', 'Pizza', 'Pudim')
#Tuplas são imutaveis#
#lanche = ('água','Refri', 'Cerveja')
print(lanche)
print(len(lanche))
for comida in lanche:
    print(f'Eu vou comer {comida}')
for c in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
for pos, comida in (enumerate(lanche)): #para enumerate, primeira variavel=posição, segunda variavel, variavel composta
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche)) #Mostando em ordem, alfabética [ele "transforma" em lista, colocando entre cochetes]
a = (1, 2, 5, 7)
b =(3, 4, 2, 6, 8)
c = a + b
print(c) #Concatenação de tuplas, em uma tupla única, na ordem da concatenação.
print(sorted(c))
print(len(c))
print(c.count(2))
print(c.index(2)) #Índice da primeira ocorrência, PODE BUSCAR POR STRINGS
print(c.index(2, 2)) #Índice da primeira ocorrência, a partir de determinado ponto.
pessoa = ('Cauan', 27, "M", 63.8) #Podemos ter dados de tipos diferentes dentro de uma tupla
#del(pessoa)#Ela pode ser apagada durante o programa. (somente INTEIRA)
print(pessoa)
