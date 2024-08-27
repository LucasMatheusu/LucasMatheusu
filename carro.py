dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
pago = (dias * 39 ) + (km * 0.90)
print('O total a pagar e de R${:.2f}'.format(pago))