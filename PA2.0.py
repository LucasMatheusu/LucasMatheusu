print('Gerador de PA')
print('-='*11)
primeiro = int(input('Primeiro termo'))
razao = int(input('Razão de PA:'))
termo = primeiro
cont = 1
while cont <= 15:
    print('{} ->'.format(termo), end='')
    termo = termo + razao
    cont += 1
print('Acabou')