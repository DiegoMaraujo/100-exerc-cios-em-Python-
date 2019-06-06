print('='*25)
print('{:^25}'.format('banco'))
print('='*25)
sac = int(input('qula valor do saque R$ '))
total = sac
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total  {totced} cedulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break
print('{:^25}'.format('Fim'))

