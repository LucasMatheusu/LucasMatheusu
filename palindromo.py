frase = str(input('digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
print('o inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindrimo')
else:
    print('A frase digitada não é um palindromo')
