from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
rankin = list()
print('Valores Sorteados')
for k, v in jogo.items():
    print(f'{k} tiro {v} o dado.')
    sleep(1)
print('/-/'*8)
rankin = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#print(rankin)
for i, v in enumerate(rankin):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)