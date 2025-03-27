print('='* 20)
print('10 TERMOS DE UMA PA')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r
for p in range (a1, decimo + 1, r ):
    print('{}'.format(p), end=(' → '))
print('FIM')