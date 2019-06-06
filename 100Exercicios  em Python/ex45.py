from random import randint
from time import sleep
itens = ('pedra', 'papal', 'tesoura')
computador = randint(0, 2)
print('''Suas opções
[0]pedra
[1]papal
[2]tesoura''')
jogador = int(input('qual sua jogada '))
print('jo')
sleep(1)
print('kem')
sleep(1)
print('po!!!!')
print('='*13)
print('o computador escolheu {} '.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
print('='*13)
if computador == 0: #pedra
    if jogador == 0:#pedra
        print('Empate ')
    elif jogador == 1:#papel
        print('jogador ganho ')
    elif jogador == 2:#tesoura
        print(' o computador ganho')
    else:
        print('jogada invalida')
elif computador == 1: #papel
    if jogador == 0:#pedra
        print('o computador ganho')
    elif jogador == 1:#papel
        print('Empate')
    elif jogador == 2:#tesoura
        print('o jogador ganho')
    else:
        print('jogada invalida')
elif computador == 2:#tesoura
    if jogador == 0: #pedra
        print('jogador ganho')
    elif jogador == 1:#papel
        print('computator ganho')
    elif jogador == 2:#tesoura
        print('empate')
    else:
        print('jogada invalida')

