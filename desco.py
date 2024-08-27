preço = float(input(' digite o preco!'))
novo = preço - (preço * 5 / 100 )
short =preço - (preço * 50 / 100 )

print(' o primeiro valor e {},  com desconto de 5% vai sair por {}S$'.format(preço, novo))
print('o valor real do short {:.1f}, com desconto de 50% fica {:.1f}'.format(preço, short))