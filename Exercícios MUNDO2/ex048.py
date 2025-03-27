#Calcular a soma de todos os números impares que são múltiplos de 3 e que se encontram entre 1 e 500
import math
soma = 0
for numero in range(0, 501):
    if numero %2 != 0 and numero % 3 == 0:
        soma = soma + numero
print('A soma de todos os números ímpares, entre 0 e 500, é de {}.'.format(soma))