num = []
maio = 0
menor = 0
for c in range(0, 6):
    num.append(int(input(f'digite um valor na posiçao {c}:')))
    if c == 0:
        maio = menor = num[c]
    else:
        if num[c] > maio:
            maio = num[c]
        if num[c] < menor:
            menor = num[c]
print(f'voce digitou os valores {num}')
print(f'O maior valor digitado foi {maio}')
for i, v in enumerate(num):
    if v == maio:
        print(f'{i}...', end='')
print()
print(f'O mneor valor digitado foi {menor}')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}....', end='')
print()