print('{:=^40} '.format('LOJA OLIVEIRA'))
preço = float(input('Preço das compras'))
print(''' FORMAS DE PAGAMENTO
[ 1 ] A VISTA
[ 2 ] a vista cartao
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera parcelada em 2x dde R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço +(preço * 20 / 100)
    totparç = int(input('Quantas prcelas ?'))
    parcela = total / totparç
    print('sua compra sera parcelada em {}x de R${:.2f}'.format(totparç, parcela))
else:
    total = preço
    print('Opçao ivalida de pagamentos. tente novamente')
print('Sua compra de {:.2f} vau custar R${:.2f} no final'.format(preço, total))
