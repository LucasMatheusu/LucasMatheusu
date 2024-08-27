print('=' * 30)
print('{:^30}'.format('Banco do lucas'))
print('==' * 30)
valor = int(input('que valor voce quer sacar? R$'))
total = valor
ced = 50
totaced = 0
while True:
    if total >= ced:
        total -= ced
        totaced += 1
    else:
        if totaced > 0:
         print(f'total de {totaced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totaced = 0
        if total == 0:
            break
print('Volte sempre ao Banco do lucas')
