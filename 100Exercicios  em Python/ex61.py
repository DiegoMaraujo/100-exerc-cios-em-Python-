print('='*20)
print('Gerador de PA')
print('='*20)
primeiro = int(input('Digite o primeiro termo '))
razao = int(input('Digete a razão da PA '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
