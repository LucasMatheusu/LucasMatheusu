print('>=<' * 40)
letreiro = str(input('Bem-Vindo, escolha seu onibus, digite 0 para continuar'))
onibus = 0
rapido = 8
conforte = 10
exprex = 5
print(f"sua tabela e ")
while onibus != 6:
    print('    [ 1 ] rapido \n'
          '    [ 2 ] conforte\n'
          '    [ 3 ] exprex\n'
          '    [ 4 ] Valores '
          '    '
          '[ 5 ] Informações\n'
          '    [ 6 ] Sair')
    onibus = int(input('Qual sua opção?'))
    # 1 Onibus rapido
    if onibus == 1:
        print(f'Voçê escolheu o onibus da modalide rapido , ele so passa em 2 linhas e vai direto a BSB, Seu valor e '
              'RS8;00')
        dinheiro = int(input('eu tenho '))
        if dinheiro > 8:
            troco = dinheiro - rapido
            print(f'seu  dinheiro R${dinheiro} e a passagem R${rapido}  seu troco e {troco} reais boa viagem')
        if dinheiro <= 8:
            deve = dinheiro - rapido
            print(f'o seu valor e {dinheiro} a passagem e {rapido} voce deve {deve}')
    # 2 Onibus conforte
    elif onibus == 2:
        print(f'O onibus conforte e o mais confortavel da nossa linha, a passagem e {conforte}')
        dinheiro = int(input('eu tenho'))
        if dinheiro > 10:
            troco = dinheiro - conforte
            print(f"seu dinheiro e R$ {dinheiro} e a passageme {conforte} seu troco e {troco}")
        if dinheiro <= 10:
            deve = dinheiro - conforte
            print(f"O seu valor {dinheiro} e a passagem e {conforte} voce deve {deve}")
    # 3 Onibus exprex
    elif onibus == 3:
        print(f'O onibus exprex e mais demorado, a passagem custa {exprex}')
        dinheiro = int(input('Eu tenho'))
        if dinheiro > 5:
            troco = dinheiro - exprex
            print(f"seu dinheiro e R$ {dinheiro} e a passagem e {exprex} seu troco e {troco}")
        if dinheiro <= 5:
            deve = dinheiro - exprex
            print(f"O seu valor {dinheiro} e a passagem e {exprex} voce deve {deve}")
    # 4 Valores
    elif onibus == 4:
        print(f" os valor sao - {conforte}R$10reais {rapido}R$8Reais ")
    # 5 Informações
    elif onibus == 5:
        print('-=' * 40)
        print('Onibus rapido, oferece rapides para chegar ao seu destino so parando em 2 pontos e assim não havendo stresse\n'
         "Onibus conforte e o mais confortavel entre os outros 2 modelos da empresa, passa em 8 pontos da cidade,\n "
        "contem ar-condiconado e poltronas bem acochoados\n"
        "o Exprex passa em todos os pontos, 12 ao total mas como demora um poucoa mais para chegar ao destino "
        "ele e mais barato")
    else:
        print('obrigado,Volte sempre')

