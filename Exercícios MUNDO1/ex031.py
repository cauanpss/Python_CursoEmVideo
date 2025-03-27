#Distancia da viagem em km, preço da passageem = 0,50/km < 200km, e 0,45 se >200k
d = int(input('Qual a distância da viagem? '))
if d >= 200:
    v = (d*0.50)
else:
    v = (d*0.45)

print('O valor da passagem é de {}'.format(v))
