lista = ('carterno', 10.70, 'Lapis ', 1.70, 'Borracha', 1.00, 'Cola', 1.80, 'tesoura', 2.50, 'caneta', 2.00)
print('-'*36)
print(f'{"LISTAGEM PREÇOS" :^30}')
print('-'*36)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print('{:.<30}'.format(lista[pos]), end='')
    else:
        print('R${:>}'.format(lista[pos]))
