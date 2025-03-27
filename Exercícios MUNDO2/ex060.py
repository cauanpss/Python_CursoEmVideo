#Ler um número e  mostrar fatorial
import math
n = int(input('Insira um número: '))
n_fatorial = math.factorial(n)
print(n_fatorial)
#-------------------------maneira burra--------------------#
n = int(input('Insira um número: '))
operador = n
fatorial = 1
while operador > 1:
    fatorial = fatorial  * operador
    operador = operador - 1
print (fatorial)