import random
print('Vamos jogar par ou impar!')
while True:
    par_ou_impar = str(input('Você quer ser par ou impar[P/I]: ').strip().lower())
    while par_ou_impar not in ('p', 'i'):
        par_ou_impar = str(input('Você quer ser par ou impar[P/I]: ').strip().lower())
    pc = random.randint(1,10)
    while True:
        try:
            j = int(input('Digite um valor:'))
            if j>= 0:
                break
        except ValueError:
            print('Valor inválido, digite um número inteiro >= 0')
    soma = int(j + pc)
    if soma % 2 == 0:
       numero = ('Par')
    if soma % 2 != 0:
       numero = ('Ímpar')
    if par_ou_impar == 'p' and soma % 2 == 0:
        print(f'O computador escolheu {pc}, a soma foi {soma}. O total é {numero}.')
        print('Jogador ganhou!')
        print('Vamos jogar novamente!\n'+'=' * 33)
    if par_ou_impar == 'p' and soma % 2 != 0:
        print(f'O computador escolheu {pc}, a soma foi {soma}. O total é {numero}.')
        print('Jogador perdeu!')
        break
    if par_ou_impar == 'i' and soma % 2 != 0:
        print(f'O computador escolheu {pc}, a soma foi {soma}. O total é {numero}.')
        print(f'Jogador ganhou!')
        print('Vamos jogar novamente!\n' +'=' * 30)
    if par_ou_impar == 'i' and soma % 2 == 0:
        print(f'O computador escolheu {pc}, a soma foi {soma}.O total é {numero}.')
        print('Jogador perdeu!')
        break
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=VERSÃO REDUZIDA-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import random

#print('Vamos jogar par ou ímpar!')

#while True:
#    par_ou_impar = input('Você quer ser par ou ímpar [P/I]? ').strip().lower()
#    pc = random.randint(1, 10)
#    j = int(input('Digite um valor: '))
#    soma = j + pc
#
#    print(f'O computador escolheu {pc}, a soma foi {soma}.')
#
#    if (par_ou_impar == 'p' and soma % 2 == 0) or (par_ou_impar == 'i' and soma % 2 != 0):
#        print('Jogador ganhou!')
#        print('Vamos jogar novamente!\n' + '=' * 33)
#    else:
#        print('Jogador perdeu!')
#        break