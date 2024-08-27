soma = 0
conta = 0
for c in range(1, 7):
    nm = int(input('digite o {} valor'.format(c)))
    if nm % 2 == 0:
        soma += nm
        conta += 1
print('voce informou {} numeros pares e a soma foi {}'.format(conta, soma))
