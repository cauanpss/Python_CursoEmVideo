print('10 TERMOS DE UMA PA')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = 0
contagem = 0
while contagem != 10:
    termo += r
    contagem += 1
    print(termo)
print('fim')
