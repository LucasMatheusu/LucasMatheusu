sexo = str(input('informe seu sexo : [M F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos, informe seu sexo')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))