palavras = ('aprender', 'progamar', 'linguagem', 'python',
            'curso', 'gratis', 'mercado')
for p in palavras:
    print(f'\nNa palavras {p.upper()} temos')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')