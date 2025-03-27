tupla = ('cauan', 'Andre', 'Daiana', 'Flora', 'Juca','Julia')
for palavra in tupla:
    print(f'\nA palavra é {palavra}, e está na posição {tupla.index(palavra)} da tupla.\nSuas vogais são: ')
    for vogal in palavra:
        if vogal in 'aeiou':
            print(vogal, end = '.')