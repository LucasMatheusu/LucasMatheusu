valores = list()
for cont in range(0, 5):
    valores.append(int(input('digite um valor')))


for c, v in enumerate(valores):
    print(f'Na posição {c} encotrei o valor {v}...')
print('Fim')