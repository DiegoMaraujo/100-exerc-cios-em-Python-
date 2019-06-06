c = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'desesis', 'desesete', 'desoito',
     'desenove', 'vinte')
while True:
    while True:
         nu = int(input('Digite um numero de 0 a 20 '))
         if 0 <= nu <= 20:
            break
         print('tente novamente', end='')
    print(f'o numero que voce digito foi  {c[nu]}')
    cont =' '
    while cont not in 'SN':
        cont = str(input('quer continuar [S/N]')).upper().strip()[0]
    if cont == 'N':
        break