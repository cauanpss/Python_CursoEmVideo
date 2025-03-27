
print('10 primeiros TERMOS DE UMA PA, e quantos mais você quiser:'.lower())
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
contagem = 0
for contagem in range(0, 10):
    print(termo, end = ' → ')
    termo += r
    contagem += 1
while True:
    nova_contagem = int(input('\nQuantos termos a mais você quer mostrar?\n(Escolha 0 se quiser finalizar o programa.):\n'))
    for _ in range(nova_contagem):
        print(termo, end =' → ')
        termo += r
        contagem += 1
    if nova_contagem == 0:
        print(f'Programa finalizado. Você exibiu {contagem} termos')
        break