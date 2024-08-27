maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('digite seu peso {}'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}KG'.format(maior))
print('O maior peso lidp foi de{}KG'.format(menor))
