print('Vamos ver se você precisa se alistar no exército.')
ano_nascimento = int(input('Em qual ano você nasceu? '))
ano_atual = int(input('Em que ano estamos? '))
tempo_para_alistamento = ano_atual - ano_nascimento
falta_para_alistamento = 18 - tempo_para_alistamento
deveria_ter_alistado = tempo_para_alistamento - 18
if tempo_para_alistamento == 18:
    print('Você deve se alistar no exército neste ano!')
elif tempo_para_alistamento < 18:
    print('Você ainda não precisa se alistar no exército. Faltam \033[31m{} anos\033[m para que você deva se alistar.'.
          format
          (falta_para_alistamento))
elif tempo_para_alistamento > 18:
    print('Você já deveria ter se alistado para o exército fazem \033[31m{} anos\033[m !'.format(deveria_ter_alistado))