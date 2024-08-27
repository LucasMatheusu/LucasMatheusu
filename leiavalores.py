nu = (int(input('Digite um numero')),
      int(input('Digite um numero')),
      int(input('Digite um numero')),
      int(input('Digite um numero')))
print(f'Voçê digitou os valores {nu}')
print(f'O valor 9 apareceu {nu.count(9)} vezes')
if 3 in nu:
    print((f'o valor 3 apareceu na {nu.index(3)} posição'))
else:
    print('o valor 3 ão foi digitado em nenhuma posição')
print('Os valores pares foram ', end='')
for n in nu:
    if n % 2 == 0:
        print(n, end=' ')
