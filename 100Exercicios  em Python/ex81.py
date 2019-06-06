lista = list()
while True:
    lista.append(int(input('Digite um valor ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]')).upper()[0].strip()
    if r == 'N':
        break
print(f' A quantidade  de elementos são {len(lista)}')
lista.sort(reverse=True)
print(f'os valores  digitados na ordem decrecente são {lista}')
if 5 in lista:
    print('O numero 5 esta na lista')
else:
    print('Esse numero não esta na lista ')