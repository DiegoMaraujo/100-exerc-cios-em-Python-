'''from time import sleep

def contagem(ini, fi, passo):
    print('-'*30)
    if passo == 0:
        passo = 1

    print(f'contagem de { ini } até { fi } de { abs(passo)} e { abs(passo)}')
    passo = abs(passo)

    if ini > fi:
        passo = passo - passo * 2
        fi = fi - 1
    else:
        fi = fi + 1

    for c in range(ini, fi, passo):
        sleep(0.6)
        print(c, end=' ')
    sleep(0.6)
    print(' Fim ')


#programa principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez sua de personalizar sua contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passos = int(input('Passos: '))

contagem(inicio, fim, passos)'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*25)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont = cont + p
        print('fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('fim')

#programa
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*20)
print('Agora é sua vez de pensonalizar a contagem: ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)