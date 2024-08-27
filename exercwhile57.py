sexo = str(input('Informe seu sexo [m/f]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('sexo inavlido, digite novamente')).strip().upper()[0]
print('sexo {} certo'.format(sexo))