#Ler ano de nascimento de 7 pessoas, e dizer quantas são, e quantas não, maior de idade.
maior_de_idade = 0
menor_de_idade = 0
ano_atual = int(input('Qual ano estamos? '))
for ano_nascimento in range (1, 8):
    ano_nascimento = int(input('em que ano a {}º nasceu? '.format(ano_nascimento)))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1
if maior_de_idade == 1:
    print('{} pessoa é maior de idade.'.format(maior_de_idade))
elif menor_de_idade == 1:
    print('{} pessoa é menor de idade.'.format(menor_de_idade))
else:
    print('{} pessoas, são maior de idade.'.format(maior_de_idade))
    print('{} pessoas, são menor de idade.'.format(menor_de_idade))
