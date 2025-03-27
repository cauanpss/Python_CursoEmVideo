print('Calcularei a média de suas duas notas, para sabermos os próximos passos de sua vida acadêmica. Para isso insira '
      'abaixo as notas da:')
p1 = float(input('Primeira prova: '))
p2 = float(input('Segunda prova: '))
m = (p1 + p2)/2
if m > 7.0:
    print('Parabéns! Você foi aprovado com média \033[32m{}\033[m!'.format(m))
elif 5.0 <= m <= 6.9:
    print('Ainda há uma chance! Infelizmente sua média foi de \033[33m{}\033[m, será necessário realizar a recuperação!'
          ''.format(m))
elif m < 5:
    print('Sua média foi de \033[31m{}\033[m. Infelizmente você foi \033[1;7mreprovado\033[m.'.format(m))
