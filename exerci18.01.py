galera = []
peso = []
maior = menor = 0
while True:
    peso.append(str(input('nome')))
    peso.append(float(input('peso')))
    if len(peso) == 0:
        maior = menor = galera[1]
    else:
        if peso[1] > maior:
            maior = peso[1]
        if peso[1] < menor:
            menor = peso[1]
    galera.append(peso[:])
    peso.clear()
    respo = str(input('quer continuar [S,N]'))
    if respo in 'Nn':
        break
print('-=' * 20)
print(f'Ao todo, voce cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maior}KG peso de', end='')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi {menor}KG. peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()


