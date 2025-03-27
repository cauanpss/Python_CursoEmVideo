nome = input('Qual seu nome completo? ')
nomema = nome.upper()
print('O nome com todas as letras maiúsculas fica: {}' .format(nomema))
nomemi = nome.lower()
print('O nome com todas as letras minúsculas fica: {}'.format(nomemi))
nomese = nome.replace(' ', '')
print('A quantidade de letras em {} é de {}'.format(nome,len(nomese)))

minha_lista = nome.split()
caracteres_primeiro_nome = (len(minha_lista[0]))
print('A quantidade de caracteres no primeiro nome é de {}'.format(caracteres_primeiro_nome))

