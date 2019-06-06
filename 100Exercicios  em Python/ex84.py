lista = list()
dados = list()
r =' '
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('='*25)
print(f'O total cadastrado foi {len(lista)}')
print(f'O maior peso foi  {maior}Kg pessoas. peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'Os menor  peso foi {menor}Kg pessoas. peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='')
print()
