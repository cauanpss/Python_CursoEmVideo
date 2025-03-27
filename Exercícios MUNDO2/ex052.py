import math
import random

print('Verificador de número primo:')
print('-=-'*20)
n = int(input('Insira um número:'))
if n == 1:
    print('Esse não é um número primo.')
elif n == 2:
    print('Este é não um número primo')
else:
    primo = True
    for p in range (2, int(math.sqrt(n))+1):
        if n % p == 0:
            primo = False
            pass
    if primo:
        print('Esse é um número primo.')
    else:
        print('Esse não é um número primo.')



