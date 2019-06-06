'''from math import factorial
n = int(input('Digite o numero para calcular seu fatorial ? '))
f = factorial(n)
print('o factorial de {} é {} '.format(n, f))'''

n = int(input('Digite um numero para calculo fatorial ? '))
c = n
f = 1
print('Calculando o fatorial {} ! = '.format(n), end='')
while c > 0:
    print(' {} '.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c # f = f * c
    c -= 1
print(' {} '.format(f))