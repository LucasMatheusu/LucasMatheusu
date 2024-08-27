from random import randint
computador = randint(0, 10)
print('sou seu pc, pensei em um numero entre 0 e 10')
print('sea que voce consegue advinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual e seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais....tente mais uma vez')
        elif jogador > computador:
            print('menos...tente mais uma vez')
print('Acertou com {} papiltes!'.format(palpites))