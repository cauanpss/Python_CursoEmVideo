print('\033[1;30;41mTeste\033[m') #para finalizar a pesonalização de cor, colocar um código 'limpo' ao final  da formatação
print('\033[4;33;44mOlá mundo')
print('\033[1;35;43mbrincando com as cores\033[m')
print('\033[30;42mEssa é uma frase com outra cor\033[m')
print('\033[mEssa é sem nenhuma variavel\033[m')
print('\033[7mEssa é só invertendo (negativo)')
#Estilizando "meio" de código:
a = 3
b = 5
print('Os valores são \033[1;33;44m{}\033[m, \033[35;42m{}\033[m, \033[4m{}\033[m'.format(a,b, b ))#Sempre FECHAR
#código de cor
#Macete para evitar códigos muito longos
nome = 'Cauan'
#Indexação abaixo será mostrada melhor posteriormente
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'brancoepreto':'\033[7m'}
print('Olá {}{}{}, muito prazer em te conhecer!'.format('\033[34m', nome, '\033[m'))
print('Olá, muito prazer em te conhecer {}{}{}'.format(cores['azul'], nome , cores['limpa']))
print('Olá {}{}{} veja que essa frase está diferente!'.format(cores['brancoepreto'], nome, cores['limpa']))