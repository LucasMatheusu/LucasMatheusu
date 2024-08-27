soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite os valores'))
    if num % 2 == 0:
        soma += num
        cont += 1
print('voce informou {} numeors pares parabens a soma foi {}'.format(cont, soma))