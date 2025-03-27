#Computador pensar em um número de 0 a 5, usuário vai tentar descobrir, e receberá uma resposta.
import random

l = [1,2,3,4,5]
r = random.choice(l)
#r = randint(0,5)  randomizar, inteiros entre 0 e 5 (sem incluir o 0)

n = int(input('Estou pensando em  um número entre 1 e 5... Será que você consegue adivinhar qual é? Vamos! Dê um palpite: '))
if n == r:
    print('Uau! Você é realmente um oráculo.')
else:
    print('Ops... Parece que não foi dessa vez, o número que eu estava pensando era {}'.format(r))
