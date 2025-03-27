produto_maior_1000 = 0
primeiro_produto = input('Qual  o nome do produto? ')
primeiro_preco = float(input('Qual preço do produto? '))
preco_total = primeiro_preco
produto_barato = primeiro_produto
if primeiro_preco > 1000:
    produto_maior_1000 += 1
menor_preco = primeiro_preco
continuar = input('Quer continuar [S/N]? ').lower()
if continuar not in ('s','n'):
        print('[ERRO] Insira um valor válido para continuar')
if continuar == 's':
    while True:
        produto = input('Qual nome do produto? ')
        preco = float(input('Qual valor do produto? '))
        preco_total += preco
        if preco > 1000:
            produto_maior_1000 =+ 1
        if preco <= menor_preco:
            menor_preco = preco
            produto_barato = produto
        continuar = input('Quer continuar [S/N]? ').lower()
        if continuar not in ('s','n'):
            print('[ERRO] Insira um valor válido para continuar')
        if continuar == 'n':
            break
else:
    pass
print(f'O total gasto foi de: {preco_total}.\nO total de produtos acima dos 1000R$ é de {produto_maior_1000}.\nO produto '
      f'mais barato foi {produto_barato}.')