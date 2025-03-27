import math
n = float(input('Digite um número fracionado: '))
p = math.trunc(n)
print (' \033[1;4;7;31;40m{}\033[m é a parte inteira deste número.'.format(p))
