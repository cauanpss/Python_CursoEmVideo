#Exibir n números de uma sequência de fibonacci
#Formula geral de fibonacci :  fn = f(n-1) + f(n-2)

#------------------------------------------------------------#

#Variáveis:
n = int(input('Quantos termos você quer exibir? '))
t1 = 0
t2 = 1
print (f'{t1} → {t2}', end= '')
contador_loops = 3
#início do código
while contador_loops <= n :
    t3 = t1 + t2
    print (f' → {t3}', end = '')
    contador_loops += 1
    t1 = t2
    t2 = t3
print(' → FIM')
