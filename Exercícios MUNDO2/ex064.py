#Digitar n números, parar quando digitar 999, dizer a soma de todos os números#
n = int(input('Digite um valor: '))
contagem = 0
sair_do_programa = False
s = n + 0
while True:
    n = int(input('Digite outro valor, se quiser parar digite 999 :'))
    if n == 999:
        break
    s = (s + n)
print(s)