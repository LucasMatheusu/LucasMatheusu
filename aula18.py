galera = list()
dado = list()
totmai = totmeno = 0
for c in range(0, 3):
    dado.append(str(input('nome')))
    dado.append(int(input('idadde')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmeno += 1
print(f'Temos {totmai} maiores e {totmeno} menores de idade')