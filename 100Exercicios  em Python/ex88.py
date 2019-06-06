from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input('Quandos jogos da sena quer fazer '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        nu = randint(1, 60)
        if nu not in lista:
            lista.append(nu)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1
for i, p in enumerate(jogos):
    print(f'{p}')
    sleep(1)