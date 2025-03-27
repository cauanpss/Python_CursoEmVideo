numero1 = input('Digite um valor: ')
numero2 = input('Digite um segundo valor: ')
sair_do_programa = False
menu = ('Escolha uma opção:\n [1] somar\n [2] multiplicar\n [3] maior\n [4] novos números\n [5] sair do programa')
while not sair_do_programa:
    print(menu)
    escolha = int(input())

    if escolha == 1 :
        soma = int(numero1) + int(numero2)
        print(f'A soma dos dois números é: {soma}')
    elif escolha == 2 :
        multiplicacao = int(numero1) * int(numero2)
        print (f'O produto dos dois números é: {multiplicacao}')
    elif escolha == 3:
        if int(numero1) > int(numero2):
            print(f'O maior número é: {numero1}')
        elif int(numero1) < int(numero2):
            print(f'O maior número é:{numero2}')
        elif int(numero1) == int(numero2):
            print('Os números são iguais.')
    if escolha == 4:
        numero1 = int(input('Digite um valor: '))
        numero2 = int(input('Digite um segundo valor: '))
    if escolha == 5:
        break