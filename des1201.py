casa = float(input('valor da casa RS$'))
salario = float(input('salario do comprador RS'))
anos = int(input('quantos anos de financiamento'))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar a casa de RS${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação sera de RS${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('emprestimo pode ser \033[32m CONCEDIDO')
else:
    print('Emprestimo \033[32m negado')