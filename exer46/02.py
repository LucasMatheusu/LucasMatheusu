print('banco do lucas')
valor = int(input('Quanto voce quer sacar ?'))
total = valor
ced = 50
totce = 0
while True:
    if total >= ced:
        total -= ced
        totce += 1
    else:
        if totce > 0:
         print(f'total de {totce} cedulas e de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
             ced = 1
        totce = 0
        if total == 0:
            break


