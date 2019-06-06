from random import randint
from time import sleep
numeros = list()

def solteio():
    for c in range(0, 10):
        numeros.append(randint(0, 10))
    print(f'Os numeros sorteados foram: ')
    for c in numeros:
        sleep(0.5)
        print(c, end=' ')
    print()
    print('-'*40)
    print(f'Os numeros pares sorteados foram: ')
def soma():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            sleep(0.5)
            print(f'{n}', end=' ')
            s = s + n
    print()
    print('-' * 40)
    print(f'A soma dos numeros pares são: {s}')




solteio()
soma()


