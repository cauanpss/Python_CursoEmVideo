for c in range (1, 7):#útlimo número não é considerado para contagem de reps, ex: (1, 6) só repetiria 5x
    print('oi', c)
print('Fim')
#Contar para trás:
for c in range (6, 0, -1):
    print ('oi', c)
print('fim')
#Pulando caracteres (pode ser positivo ou negativo)<->(pra frente/pra trás)
for c in range (7, 0, -2):
    print(c)
print('fim')
#
n = int(input('Digite um número: '))#Podemos usar este valor para "for"
for c in range (0, n+1):# +1 utilizado para contornar a questão de não contar o último caractere. Melhorar a interação
    # usuário/máquina
    print(c)
print('fim')
#input do range é possível
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')
#input dentro de 'for'
s = 0
for c in range (0, 3):
    n = int(input('Digite um valor: '))
    s += n #forma abreviada de digitar s = s + n
print('A soma de todos os números é {}.'.format(s))