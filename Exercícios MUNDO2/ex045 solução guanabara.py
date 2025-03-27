from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-='*20)
jogador = int(input('Qual é a sua jogada?'))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*20)
if computador == 0:#Computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence!')
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('EMPATE!')
else:
    print('Jogada inválida!')