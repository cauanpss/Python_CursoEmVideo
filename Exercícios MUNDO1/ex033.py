#Ler três números, dizer o maior e o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

nmax = max(n1, n2, n3)
nmin = min(n1, n2, n3)

print('O maior número é {}, e o menor número é {}'.format(nmax,nmin) )

