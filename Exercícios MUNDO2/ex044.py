#Verificar valor do produto em seu preço normal, e em condição de sua forma de pagamento. dinheiro/cheque 10% desconto.
#A vista no cartão 5%, até 2x preço normal. 3x ou mais juros de 20%
valor_normal = float(input('Qual o valor do produto?'))
valor_no_dinheiro = valor_normal - ((valor_normal/100) * 10)
valor_cartao = valor_normal - ((valor_normal/100)*5)
valor_2x = valor_normal
valor_3x = valor_normal + ((valor_normal/100)*20)
forma_de_pagamento = str(input('Escolha a forma de pagamento:\n'
                               '(1)-Para pagamento em dinheiro ou cheque.\n'
                               '(2)-Para pagamento a vista no cartão.\n'
                               '(3)-Para pagamento no cartão em até 2x sem juros.\n'
                               '(4)-Para pagamento parcelado em 3x ou mais, com juros.\n'
                               ' '))
if forma_de_pagamento == '1':
    print('O total fica de {} Reais'.format(valor_no_dinheiro))
elif forma_de_pagamento == '2':
    print('O total fica de {} Reais'.format(valor_cartao))
elif forma_de_pagamento == '3':
    print('O total fica de {} Reais'.format(valor_2x))
elif forma_de_pagamento == '4':
    print('O total fica de {} Reais'.format(valor_3x))
