import math

a = float(input('Qual o valor do ângulo? '))
s = (math.sin(a))
c = math.cos(a)
tg = math.tan(a)
print('O seno de {:.2f} é igual a {:.2f}\nO cos é igual a {:.2f}\nA tangente é igual a {:.2f} '.format(a,s,c,tg))
