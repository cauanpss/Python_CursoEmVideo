import random
numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
print(f'Os números sorteados foram: ')
for n in numeros:
    print(n, end = ' ')
print(f'\nO menor número é {sorted(numeros)[0]}.')
print(f'O maior número é {sorted(numeros)[3]}.')

#####################################----GUANABARA SOLUÇÕES----#####################################################
import random
numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
print(f'Os números sorteados foram: ')
for n in numeros:
    print(n, end = ' ')
print(f'\nO menor número é {min(numeros)}.')
print(f'O maior número é {max(numeros)}.')