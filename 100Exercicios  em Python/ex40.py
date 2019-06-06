n1 = float(input('Digite a primeira nota ? '))
n2 = float(input('digite a segunda nota ? '))
m = (n1 + n2) / 2
print('Entre primeira nota  {} e segunda nota  {} a media é {}'.format(n1, n2, m))
if m >= 7:
    print('Aluno aprovado media  ')
elif m >= 5 and m < 7:
    print('Alunao em recuperação ')
elif 5 < m:
    print('Aluno reprovado a media ')
