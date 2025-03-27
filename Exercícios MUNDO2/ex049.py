#Tabuada de 1 a 10, com número que usuário escolher.
n = int(input('Digite um número para ver sua tabuada de 1 até 10x: '))
for t in range (1, 10+1):
    r = (n * t)
    print(n, '*', t, '=', r)