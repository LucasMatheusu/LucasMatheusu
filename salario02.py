salario = float(input('digite seu salario'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('seu salario era {}, agora e {}'.format(salario, novo))
