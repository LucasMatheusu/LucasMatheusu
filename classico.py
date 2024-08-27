n1 = float(input('Primeira nota'))
n2 = float(input('Segunda nota'))
media = (n1 + n2 ) / 2
print('Tirando {:.1f} e  {}, a media do aluno e {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('o aluno esta em \033[35m recuperação')
elif media < 5:
    print('O aluno esta \033[34m reprovado')
elif media >= 7:
    print('O aluno esta \033[32m aprovado')
