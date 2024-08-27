resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    nm = int(input('digite um numero'))
    soma += nm
    quant += 1
    if quant == 1:
        maior = menor = nm
    else:
        if nm > maior:
            maior = nm
        if nm < menor:
                  menor = nm
    resp = str(input('quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('voce digitou {} numeros e a media foi {}'.format(quant, media))
print('o maior valor foi {} e o menor foi {}'.format(maior, menor))
print('acabou')