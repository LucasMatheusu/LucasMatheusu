preço = ('lapis', 1.75,
         'borracha', 2,
         'caderno', 3,
         'caneta', 9,
         'Mochila', 15)
print('-' * 25)
print(f'{"PREÇO ESCOLARES":40}')
for pos in range(0, len(preço)):
    if pos % 2 == 0:
        print(f'{preço[pos]:.<20}', end='')
    else:
        print(f'RS${preço[pos]:>7.2f}')