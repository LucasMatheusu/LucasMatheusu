print('{:^30}'.format('RODOVIARIA'))
print(' O onibus1 passa em todas as paradas, O onibus2 passa em metade,  onibus3 e o mais rapido')
carteira = int(input('quanto voce tem na sua caretira R$?'))
onibus1 = 6
onibus2 = 9
onibus3 = 15
troco = carteira
deve = carteira
if carteira > onibus1:
     troco = carteira - onibus1
     print(f'seu troco foi {carteira} - {onibus1} = {troco}')
elif carteira < onibus1:
    deve = onibus1 - carteira
    print(f'voce deve {deve}')
    print('pague ou desca')
print('Obrigado')



