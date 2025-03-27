frase = input('Digite uma frase: ').upper()
#Quantas vezes aparece a letra a?
a = frase.count('A')
frase.strip()
print ('A letra A, aparece {} vezes na frase'.format(a))
#Em que posição ela aparece a primeira vez?
p1 = frase.find('A') + 1
print ('O "A" aparece pela primeira vez na posição {} '.format(p1))
#Em que posição ela aparece a ultima vez?
p2 = frase.rfind('A') +1
print ('e pela ultima vez aparece na posição {}'.format(p2))
