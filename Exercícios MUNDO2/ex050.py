#Programa que leia 6 numeros int, mostre a soma dos pares, e desconsidere os impares
import math
soma = 0
for n in range (0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
if soma == 0:
    print('Todos os valores são ímpares.')
else:
    print('A soma dos números pares digitados é {}'.format(soma))