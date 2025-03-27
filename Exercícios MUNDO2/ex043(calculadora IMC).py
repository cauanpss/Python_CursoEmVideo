print('Olá! Hoje vamos calcular o seu IMC!')
a = float(input('Por favor, digite a sua altura: '))
p = float(input('Me informe o seu peso: '))
imc = (p/(a*a))
print ('O seu imc é de {:.2f} isso significa que:'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do  peso ideal.')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal.')
elif 25 < imc <= 30:
    print('Você está com  sobrepeso.')
elif 30 < imc <=40:
    print('Se atente, você está com obesidade! Isso pode trazer riscos a sua saúde.')
elif 40 < imc:
    print('Infelizmente no momento, você está no estágio da obesidade mórbida. Isso pode trazer sérios riscos a sua saú'
          'de. Procure acompanhamento médico o mais breve possível.')
