nome = str(input('Digite seu nome')).strip()
print('a Letra a aparece {} vezes na frase '.format(nome.count('a')))
print('a orimeira letra a apareceu na posicaçao {}'.format(nome.find('a')+1))
print('a ultima letra a apareceu na posiçao {}'.format(nome.rfind('a')))