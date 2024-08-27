n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor:'))
opção = 0
while opção != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multipicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair é a sua opção''')
    opção = int(input('>>>>Qual e a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} e {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A soma entre {} x {} e {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor e {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primerio valor:'))
        n2 = int(input('segundo valor'))
    elif opção == 5:
     print('finalizado')
    else:
        print('Opção invalida')
    print('=-='*10)
print('fim do progama, volte sempre')