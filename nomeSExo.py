somaidade = 0
mediaida = 0
maioridade = 0
nomevel = ''
totmulh20 = 0
for p in range(1, 5):
    print('----{} Pessoa-----'.format(p))
    nome = str(input('nome')).strip()
    idade = int(input('idade:'))
    sexo = str(input('Sexo [M,F}')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevel = nome
    nomevel = nome
    if sexo in 'Ff' and idade < 20:
        totmulh20 += 1
mediaida = somaidade / 4
print('A media de idade dp grupo e de {} anos'.format(mediaida))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevel))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totmulh20))

