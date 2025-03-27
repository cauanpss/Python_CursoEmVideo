n = float(input('Digite um valor: '))
contagem = 1
s = n + 0
sair_do_programa = False
maior_numero = n
menor_numero = n
while True :
    continuar = input('Quer continuar? [S/N]').strip().lower()
    if continuar != 'n' and continuar != 's':
        continuar = input('Digite S ou N: ')
    if continuar == 'n':
        break
    n = float(input('Digite outro valor:'))
    s += n
    if n > maior_numero:
        maior_numero = n
    if n < menor_numero:
        menor_numero = n
    contagem += 1
m = float(s / contagem)
print(f'A média entre os números digitados é {m}, o maior número foi {maior_numero}, e o menor número foi {menor_numero}'
      f'')