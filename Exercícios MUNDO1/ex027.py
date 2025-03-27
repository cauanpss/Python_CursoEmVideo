n = input('Digite seu nome completo:').title().strip()
print ('Olá {} muito prazer em conhece-lo.'.format(n.title()))
#print (n1)
#Identifique o primeiro nome:
ns = n.split()
print ('Seu primeiro nome é: {}'.format(ns[0]))
#Identifique o ultimo nome
print ('Seu ultimo nome é: {}'.format(ns[-1]))

# O - pode ser usado para contar de trás pra frente, -1 ultimo -2 penúltimo e assim por diante.