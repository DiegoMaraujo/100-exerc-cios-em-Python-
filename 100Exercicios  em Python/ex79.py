lista = list()
while True:
    num = (int(input('Digite um valor ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso ')
    else:
        print('Valor existente ')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).upper()[0].strip()
    if resp in 'N':
        break
lista.sort()
print(f'os numeros digitados foi {lista} ')
