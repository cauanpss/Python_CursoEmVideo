#Leia a velocidade de um carro, se passar dos 80km é multa, multa custa 7R$ por cada km acima do permitido.
v = int(input('Qual a velocidade registrada pelo veículo? '))
m = (v-80) * 7
if v >= 80:
    print('O seu veículo foi multado, o valor da multa é de: {}'.format(m))
else:
    print('O seu veículo não foi multado.')