#Jogar jokenpo e exibir mensagem de vitória ou derrota
import random

jogadas = ['pedra', 'papel', 'tesoura']
pc = random.choice(jogadas)
print('Vamos jogar pedra, papel ou tesoura!')
jogador = str(input('Qual sua jogada? ')).lower()
if pc == 'pedra' and jogador == 'tesoura':
    print ('A máquina é uma máquina! Você perdeu, seu lixo!')
elif pc == 'pedra' and jogador == 'papel':
    print ('Eu sou mesmo um bot. Vitória sua!')
elif pc == 'tesoura' and jogador == 'pedra':
    print('Eu sou mesmo um bot. Vitória sua!')
elif pc == 'tesoura' and jogador == 'papel':
    print('A máquina é uma máquina! Você perdeu, seu lixo!')
elif pc == 'papel' and jogador == 'pedra':
    print('A máquina é uma máquina! Você perdeu, seu lixo!')
elif pc == 'pedra' and jogador == 'papel':
    print('Eu sou mesmo um bot. Vitória sua!')
elif jogador == pc:
    print('Boa tentativa, esse foi um empate!')
print('A minha jogada foi {}.'.format(pc))