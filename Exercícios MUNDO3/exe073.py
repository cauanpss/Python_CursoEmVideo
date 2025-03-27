times = ('Palmeiras', 'Grêmio', 'Atlético Mineiro', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico'
        ' Paranaense', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Santos',
        'Vasco da Gama', 'Bahia', 'Goiás', 'Coritiba', 'América Mineiro')
print('Os 5 primeiros colocados são:')
for colocados in times[:5]:
    print(colocados)
print('=-' * 20)
print('Os ultimos 4 colocados são: ')
for ultimos in times[16:]:
    print(ultimos)
print('=-' * 20)
print('Todos os times em ordem alfabética: ')
print(sorted(times))
print('=-' * 20)
print(f'O Bahia está na {times.index('Bahia')}º posição.')