#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('Olá, agora analisaremos se as 3 retas podem formar ou não um triângulo.')
r3 = float(input('Qual o comprimento da maior  reta? '))
print('Insira abaixo, separadamente, o comprimento das outras duas retas: ')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
# verificar se a soma de dois lados é maior que o terceiro lado
if (r1+r2)>r3:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')
