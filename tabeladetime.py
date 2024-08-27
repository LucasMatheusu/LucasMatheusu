times = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Flamengo', 'Atlético-MG', 'Athletico-PR', 'Fluminense',
         'Fortaleza', 'Cuiabá', 'São Paulo', 'Internacional''Cruzeiro', 'CorinthiansBahia', 'Santos', 'Goiás',
         'Vasco', 'Coritiba'
         , 'América-MG')
print(f'lista de times: {times}')
print('-=' * 14)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 14)
print(f'Os quatros ultimos são: {times[-4:]}')
print('-=' * 14)
print(f'times em ordem alfabeticas: {sorted(times)}')
print('-=' * 14)
print(f'O sao paulo esta na {times.index("São Paulo")+1} posiçao')