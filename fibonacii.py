print('-='*20)
print('Sequenci de Fibonacci')
print("-="*20)
n = int(input('Qual numero voce quer mostrar'))
t1 = 0
t2 = 1
print('~'*20)
print("{} -> \033[34m{}".format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> \033[34m{}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print("-> FIm")
print('-='*20)