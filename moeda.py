real = float(input(" quanto de dinheiro voce tem na carteira?"))
dolar = real / 5.17
e = real / 5.45
print(' com R${:.2f} voçe pode comprar US${:.2f} e tambem fica {:.8}e'.format(real, dolar, e))
