#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
#a R$1250, 00, calcule um aumento de 10 %.Para os inferiores ou iguais, o aumento é  de 15 %.
print('Olá, vamos calcular o seu aumento salarial!')
salario = float(input('Qual o seu salário atual? '))
if salario <= 1250.00:
    porcentagem = 15
if salario > 1250.00:
    porcentagem = 10
aumento = salario + ((salario/100)*(porcentagem))
print('O seu salário atual é {}, e com o devido  aumento, totaliza {}.'.format(salario,aumento))