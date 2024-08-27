valores = []
while True:
    valores.append(int(input('Digite um valor')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores da ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')
