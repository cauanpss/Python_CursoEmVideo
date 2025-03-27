print('Vamos verificar a tabuada!\nPara encerrar o programa, digite um valor negativo')
while True:
    n = int(input('Você quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for tabuada in range (0, 10):
        t = n * tabuada
        print (t)
print ('O programa foi finalizado!')