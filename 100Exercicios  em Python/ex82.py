lista1 = list()
pares = list()
impares = list()
while True:
    lista1.append(int(input('Digite um numero ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar [S/N]')).upper()[0].strip()
    if r == 'N':
        break
for i, v in enumerate(lista1):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os numero são {lista1}')
print(f' os numeros pares é {pares}')
print(f'Os numeros impares é {impares}')
