v=float(input('Informe o valor do produto: '))
#d=float(input('Informe o valor do desconto'))
d=5/100
vd=v-(v*d)
print('O \033[31mproduto\033[m selecionado com o desconto aplicado, fica no valor de {}R$'.format(vd))
