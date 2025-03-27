print('Olá vamos descobrir quanto de tinta é necessário para pintar a sua parede!')
l=float(input('Qual o comprimento da sua parede? '))
a=float(input('E qual a altura? '))
ar=l*a
t=ar/2
cores = {'verde':'\033[32;1;46m',
        'azul' : '\033[34;1;40m',
         'limpa':'\033[m'}
print('Você vai precisar de {}{}{} L de tinta para pintar sua parede, que tem um total de {}{}{}m²'.format(cores['azul'
], t, cores['limpa'], cores['verde'], ar, cores['limpa']))
