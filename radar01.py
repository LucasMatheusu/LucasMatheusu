carro = float(input('velocidade do primeiro carro foi '))
carrob = float(input('velocidade do segundo carro foi'))
if carro >80:
    print('O primeirro foi multado, sua velocidade foi de {}km '.format(carro,))
else:
    print('O primeiro carro nao foi multado! Boa viagem ')
if carrob >80:
    print('O segundo carro foi multado,sua velocidade foi de {}KM'.format(carrob))
else:
    print('O segundo carro nao foi multado! Boa viagem')