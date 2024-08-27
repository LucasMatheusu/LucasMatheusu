from random import randint
comput = randint(0, 10)
print('Sou seu computador.... Acabei de pensar um nmr entre 0 e 10')
print('consegue advinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual e o seu palpite ?'))
    palpites += 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('mais... tente mais uma vez')
        elif jogador > comput:
            print('menos... tente mais uma vez')
print('voce acertou com {} tantos palpites'.format(palpites))
