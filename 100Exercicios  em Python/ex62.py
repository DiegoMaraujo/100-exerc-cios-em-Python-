print('GERADOR DE PA ARITIMETICA')
print('='*20)
primeiro = int(input('digite o primeio termo '))
razao = int(input('digite a razão '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quandos termo voce quer contar '))
print('Progresão finalizada com um total {} '.format(total))