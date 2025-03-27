print ('Vamos converter um número em binário, hexadecimal ou octal!')
n = int(input('Informe o valor inteiro: '))
escolha = str(input('Para binário escolha (1)\n'
                    'Para octal escolha (2)\n'
                    'Para hexadecimal escolha (3)\n'
                    ''))
if escolha == ('1'):
    print(bin(n)[2:])
elif escolha == ('2'):
    print(oct(n)[2:])
elif escolha == ('3'):
    print(hex(n)[2:])
print('Obrigado!')
