nmr = int(input('Digite um numero inteiro'))
print('''Escolha umas das bases para conversão
[ 1 ] converter para binario
[ 2 ] converter para OCTal
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('sua opção'))
if opçao == 1:
    print('{} convertido para BINARIO e igual a {}'.format(nmr, bin(nmr)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL e igual a {}'.format(nmr, oct(nmr)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(nmr, hex(nmr)[2:]))
else:
    print('opçao invalida')