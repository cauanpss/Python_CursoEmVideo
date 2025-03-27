#Solução curso em vídeoo:
n1 = int(input('Insira um número: '))
n2 = int(input('Insira um segundo número: '))
n3 = int(input('Insira um terceiro número: '))
# Verificando o menor número
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# Verificando o maior número
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
#Existe um problema nessa solução. Quando os números são iguais, a resposta não é precisa. Solução com max e min é melhor,
# e  mais compacta
