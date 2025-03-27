#Aprovar empréstimo para compra de casa. O programa pergunta *valor da casa, salário, e quantos anos ele vai pagar*
#Calcular prestação mensal, sabendo que ela não pode exceder 30% do salário. Se exceder, empréstimo engado.
print('Olá, vamos verificar a possibilidade de um empréstimo!')
valor_casa = float(input('Qual valor do imóvel? '))
salario = float(input('Qual seu salário atual? '))
meses = float(input('Em quantos meses você deseja pagar? '))
parcela = valor_casa / meses

if salario < (parcela / 100) * 30:
    print('Seu empréstimo foi negado.')
elif salario >= (parcela / 100) * 30:
    print('Parabéns, seu empréstimo foi aprovado!')
print('Obrigado pela sua consulta!')