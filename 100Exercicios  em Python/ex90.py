aluno = dict()
aluno['nome'] = str(input('Nome:  '))
aluno['media'] = float(input(f'Media do aluno {aluno["nome"]}: '))
if aluno['media'] <= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


