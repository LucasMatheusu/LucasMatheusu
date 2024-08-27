tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = " "
    while resp not in 'S/N':
        resp = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pesoa com mais de 18 anos {tot18}')
print(f'Ao todo temos {totH} homens cadastrado')
print(f'e temos {totM20} mulheres com menos de 20 anos')
