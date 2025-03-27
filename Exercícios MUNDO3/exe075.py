while True:
    try:
        numeros = (int(input('Digite um número: ')),
                   int(input('Digite outro número: ')),
                   int(input('Digite mais um número: ')),
                   int(input('Digite o último número: ')))
        break
    except ValueError:
        print('Entrada inválida. Digite somente números inteiros.')
print(f'Você digitou os números {numeros}.')
recorrencia = numeros[0]
print(f'O primeiro número aparece {numeros.count(recorrencia)} vezes.')
if 3 in numeros:
    print(f'O número 3 aparecece primeiro na posição {numeros.index(3)}.')
contagem_pares = 0
for pares in numeros:
    if pares %2 == 0:
        contagem_pares += 1
print(f'A quantidade de números pares é: {contagem_pares}.')
