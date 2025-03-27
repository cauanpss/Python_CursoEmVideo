primeiro_peso = float(input('Qual peso da 1º pessoa? '))
maior_peso = primeiro_peso
menor_peso = primeiro_peso
for pessoa in range(0,5 ):
    pessoa = float(input('Qual peso da {}º pessoa? '.format(peso)))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso
    else:
        pass
if menor_peso == maior_peso:
        print('Os pesos são iguais')
else:
    print('O maior peso é {}'.format(maior_peso))
    print('O menor peso é {}'.format(menor_peso))