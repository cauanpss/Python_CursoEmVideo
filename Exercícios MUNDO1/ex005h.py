print('Parabéns! Seu salário recebeu uma bonificação, confira abaixo:')
s=float(input('Informe o valor do seu salário: '))
a=15/100
sa=s+(s*a)
va=s*a
print('O seu \033[33;1;4msalário\033[m atualizado, ficou no valor de {:.2f}, o montante do seu aumento foi de {:.2f}'
      .format(sa,va))

