from random import randint
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteador foram :')
for n in sorteio:
    print(f'{n}')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')