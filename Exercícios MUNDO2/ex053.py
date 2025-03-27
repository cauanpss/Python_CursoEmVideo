#Verificador de palindromo (ex: A torre da derrota, apos a sopa
frase = str(input('Digite uma frase, vamos verificar se ela é um palíndromo: ').lower().strip().replace(' ', ''))
frase_contrario = frase[::-1]

if frase == frase_contrario:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')