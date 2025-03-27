numero01=float(input('Qual o primeiro número?'))
numero02=float(input('Qual o segundo número?'))
resultado=numero01+numero02
print('A soma dos dois números é:', resultado)
#Desafio da cores:
cores = {'vermelho' : '\033[31:40m',
         'verde' : '\033[32:40m',
         'limpa': '\033[m'}
#print('A soma do número',numero01,'e do número',numero02,'é: {}'.format(resultado))
print('A soma de {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['vermelho'],numero01, cores['limpa'], cores['vermelho'],
numero02, cores['limpa'], cores['verde'], resultado, cores['limpa']))


