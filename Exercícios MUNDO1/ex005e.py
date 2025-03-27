r=float(input('Digite um valor em R$: '))
d=float(input('Qual o valor do dolar atualmente?'))
dc=r/d
print('A quantide de dólares que você pode comprar com \033[32;1;40m{}R$\033[m sabendo que o dólar está a \033[32;40;1m'
      '{}R$\033[m, é: \033[1;33m{:.2f}U$\033[m'.format(r,d,dc))
