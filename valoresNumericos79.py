num = list()
while True:
    n = int(input('digite esse valor'))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('valor duplicado, não vou adicionar')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Voce digitou os valores {num}')