from random import randint
v = 0
while True:
    jogador = int(input('diga um valor'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar[P/I]')).strip().upper()
    print(f'voce jogou {jogador} e o computador{computador} total de {total}', end='')
    print('DEU par'if total % 2 == 0 else 'DEU impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu')
            v += 1
        else:
            print('voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('vamor jogar novamente')
print(f'Game over! voce venceu {v} vezes')
