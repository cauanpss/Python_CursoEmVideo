#Computador pensar em um número de 0 a 10, usuário vai inserir número até descobrir, e receberá uma resposta.
import random
numeros = list(range(1,10))
numero_sorteado = random.choice(numeros)
tentativas = 1
#numero_sorteado  = random.randrange(1,10)
#print(numero_sorteado)
jogador = int(input('Digite um número entre 1 e 10 e tente adivinhar qual estou pensando: '))
while jogador != numero_sorteado :
    print('Quase lá! Tente mais uma vez:')
    tentativas += 1
    jogador = int(input())
if tentativas == 1:
    print('Parabéns! Você acertou de primeira!')
else:
    print(f'Parabéns! Voce acertou, e  precisou de {tentativas} tentativas para acertar!')