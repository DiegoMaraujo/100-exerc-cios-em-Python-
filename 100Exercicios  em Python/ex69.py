total18 = totalm = totalf = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input(' Sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalm += 1
    if sexo == 'F' and idade < 20:
        totalf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continua [S/N]')).strip().upper()[0]
    if resp == 'N':
            break
print(f'o total de homens maires de 18 {total18}')
print(f'o total de homens cadastrado foi {totalm}')
print(f'o total de mulheres menores foi {totalf}')
