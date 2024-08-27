nm = int(input('Digite um numero:'))
tot = 0
for c in range (1, nm + 1):
    if nm % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisivel {} vezes'.format(nm, tot))
if tot == 2:
    print('E por isso ele e PRIMO')
else:
    print('E por isso ele não e PRIMO')

