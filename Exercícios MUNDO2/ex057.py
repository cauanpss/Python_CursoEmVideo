sexo = input('Qual seu sexo? ').strip().lower()[0]
while not sexo in ('m','f'):
    sexo_valido = input('Informe um valor válido: ')
    sexo = sexo_valido
print('fim')
#-----------------------------------CORREÇÃO-----------------------------------------
#sexo = input('Qual seu sexo? ').lower()
#while not sexo in ('m','f'):
#  print('Informe um valor válido(m/f: ')
#   sexo = input('Qual  seu sexo? ').lower()
#print('fim')
