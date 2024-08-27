from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0 , 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual e a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' * 11)
print('computador jogou {}'.format(itens[pc]))
print('o jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida')

elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida')

elif pc == 2:
    if jogador == 0:
     print('JOGDOR VENCE')
elif jogador == 1:
    print('COMPUTADOR VENCE')
elif jogador == 2:
     print('EMPATE')
else:
     print('Jogada invalida')