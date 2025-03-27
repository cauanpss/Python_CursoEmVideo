
#verificar se um ano é bisexto

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print ("Esse ano é bissexto")
        else:
            print ("Esse ano não é bissexto")
    else:
        print ("Esse ano é bissexto")
else:
    print ("Esse ano não é bisexto")