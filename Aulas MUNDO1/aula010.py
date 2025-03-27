nome = str(input('Qual é o seu nome? '))
if nome == 'Cauan':
    print('Que nome lindo você tem!')
    print(
        'Vamos lá {}. Me informe as notas das 3 provas, que te direi se foi ou não, aprovado nesse semestre!'.format(nome))
else:
    print('Seu nome é tão normal...')
    print('Bom dia {}!'.format(nome))
    print('Vamos lá. Me informe as notas das 3 provas, que te direi se foi ou não, aprovado nesse semestre!')
n1 = float(input('Qual a nota da primeira prova? '))
n2 = float(input('Qual a nota da segunda prova? '))
n3 = float(input('Qual a nota da terceira prova? '))
m = (n1+n2+n3)/3
if m >= 6:
    print('Parabéns {}! Você teve uma média de {:.1f}, e foi aprovado!'.format(nome,m))
else:
    print('Desculpe {}, mas a sua média foi de {:.1f}, e ficou abaixo do necessário para ser aprovado. Infelizmente, será'
          'necessário repetir o semestre!'.format(nome,m))