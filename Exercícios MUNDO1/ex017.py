import math
cores = {'vermelhosub' : '\033[31;1;4;40m', 'limpa' : '\033[m', 'azulneg' : '\033[1;34;40m'}

cco = float(input('Qual o comprimento do cateto oposto? '))
cca = float(input('Qual o comprimento do cateto adjacente?'))
h = math.sqrt((cco**2)+(cca**2))
print('O comprimento da {}hipotenusa{} é igual {}{:.4f}{}'.format(cores['vermelhosub'], cores['limpa'], cores
['azulneg'], h, cores['limpa']))
