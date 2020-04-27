r1 = float(input('Primeiro seguimento: '))
r2 = float(input('segundo seguimento: '))
r3 = float(input('terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('os seguimentos acima pode formar um triangulo', end='')# não vai ter fim alinha
    if r1 == r2 and r2 == r3: # r1 == r2 == r3 pode simplificar
        print(' Equilatero ')
    elif r1 != r2 and r2 != r3 and r1 != r3: # r1!=r2!=r3!=r1
        print(' Escaleno ')
    else:
        print(' issoceles ')
else:
    print('Não podem formar um triangulo')