print('Olá! Vamos ver em qual categoria o atleta se encaixa. ')
ano_atual = int(input('Em qual ano estamos? '))
ano_nascimento = int(input('Em qual ano o atleta nasceu? '))
idade = (ano_atual - ano_nascimento)
if idade <= 9:
    print('O atleta se encaixa na categoria \033[33mmirim\033[m, que vai até os \033[34m9\033[m anos.')
elif 9 < idade  <= 14:
    print('O atleta se encaixa na categoria \033[33minfantil\033[m, que vai até os 14 anos.')
elif 14 < idade <= 19:
    print('O atleta se encaixa na categoria \033[33mjuvenil\033[m, que vai até os 19 anos.')
elif 19 < idade  <= 20:
    print('O atleta se encaixa na categoria \033[33msênior\033[m, que vai até os 20 anos.')
elif idade > 20:
    print('O atleta se encaixa na categoria \033[33msênior\033[m, que é a partir dos 20 anos')