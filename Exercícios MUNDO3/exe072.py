extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    try:
        n = int(input('Digite um valor entre 0 e 20: '))
        if 0 <= n <= 20:
            break
    except ValueError:
        print('Digite um valor numérico')
print(extenso[n])
