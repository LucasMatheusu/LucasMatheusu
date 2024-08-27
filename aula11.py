velocidade = float(input('sua velocidade foi'))
if velocidade > 200:
    multa = velocidade + (velocidade * 5.50 / 100)
    print('sua velocidade foi  {} e voce foi multado em \033[7;34m {}\033[m'.format(velocidade, multa))
else:
    print("\033[31;40m boa viagem!\033[m")

