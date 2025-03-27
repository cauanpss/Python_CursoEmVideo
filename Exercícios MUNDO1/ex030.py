#Leia um número e diga se é par ou impar
from operator import truediv

n = int(input('Digite um numero: '))
if  n % 2 == 0 :
    print('O número é par.')
else:
    print('O número é impar')