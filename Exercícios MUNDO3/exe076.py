produtos = ()
while True:
    try:
        produto_nome = input('Qual o nome do produto? ').title()
        produto_preco = float(input('Qual o preço do produto?  '))
        novo_produto = (produto_nome, produto_preco)
        produtos += novo_produto
    except ValueError:
        print('tente novamente')
        continue
    while True:
        continuar = input('Deseja inserir mais produtos [s/n]? ').lower()
        if continuar not in 'sn':
            print('Responda com [s/n]')
        if continuar == 's':
            break
        if continuar == 'n':
            break
    if continuar == 's':
        pass
    if continuar == 'n':
        break
print('-' * 30)
print('----LISTA DE PREÇOS----')
for pos in range (0, len(produtos)):
    if pos %2 == 0:
        print(f'{produtos[pos]:.<20}', end='')
    else:
        print(f'R${produtos[pos]:>.2f}')
