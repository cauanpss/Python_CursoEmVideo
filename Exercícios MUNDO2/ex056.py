#input = nome, idade e sexo de 4 pessoas, output =  média de idade do grupo, homem mais velho, mulheres abaixo de
# 20 anos
maior_idade = 0
total_idade = 0
homem_mais_velho = ''
maior_idade_homem = 0
mulheres_menores_20 = 0

for pessoa in range (1, 5):
    nome = input('Qual seu nome? ')
    idade = int(input('Idade? '))
    sexo = input('Sexo[M/F]? ').lower()

    total_idade += idade

    if idade > maior_idade:
        maior_idade = idade

    if sexo == 'm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_menores_20 += 1


media_idade = int(total_idade/4)
print('A maior idade do grupo é: {} '.format(maior_idade))
print('O nome do homem mais velho é: {}'.format(homem_mais_velho))
print('A média de idade do grupo é: {}'.format(media_idade))
print('O número de mulheres menores de 20 anos é: {}'.format(mulheres_menores_20))