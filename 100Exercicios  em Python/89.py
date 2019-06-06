ficha = list()
nota1 = 0
nota2 = 0
media = 0


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('*'*30)
print(f'{"No.":<4} {"NOME":<10}{"MEDIA":8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
print('*'*30)

while True:
    print('-'*30)
    op = int(input('Que ver a ficha de qual aluno ([999] para Interoomper: )'))
    if op == 999:
        print('FINALIZADO')
        break
    if op <= len(ficha) -1:
        print(f'notas do {ficha[op][0]} foi {ficha[op][1]}')
print('-'*30)
