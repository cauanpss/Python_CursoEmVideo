maiores_18 = 0
m_menores_20 = 0
homens = 0
print(('=' * 10) + 'VAMOS CADASTRAR PESSOAS:' + ('=' * 10) )
while True:
    print (('=' * 20 ) + '\nCADASTRE UMA PESSOA\n' + ('=' * 20))
    while True:
        try:
            idade = int(input('Digite a idade: ').strip().lower())
            break
        except ValueError:
            print('[ERRO] Insira um valor válido para ''Idade')
    while True:
        sexo = input('Digite o sexo[M/F]: ').strip().lower()
        if sexo in ('m','f'):
            break
        else:
            print('[ERRO] Insira um valor válido para ''sexo')
    while True:
        continuar = input('Quer continuar [S/N]: ').strip().lower()
        if continuar in ('s','n'):
            break
        else:
            print('[ERRO] Insira um valor válido  para continuar.')
    if idade >= 18 :
        maiores_18 += 1
    if idade < 20 and sexo == 'f':
        m_menores_20 += 1
    if sexo == 'm':
        homens += 1
    if continuar == 'n':
        break
print(f'O número de mulheres menores de 20 anos é {m_menores_20}.\nO número de pessoas acima dos 18 anos é {maiores_18}.'
      f'\nO número total de homens é {homens} ')