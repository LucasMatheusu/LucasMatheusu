aluno = dict()
aluno['nome'] = str(input('nome'))
aluno['media'] = float(input(f'Media de {aluno["nome"]}'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} e igual a {v}')
