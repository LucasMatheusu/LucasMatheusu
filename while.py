n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite o valor'))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} par e {} impar'.format(par, impar))


