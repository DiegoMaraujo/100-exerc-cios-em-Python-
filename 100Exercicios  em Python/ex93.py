jogador = dict()
partidas = list()
totg = 0
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantos partidas o{jogador["nome"]} jogou ?'))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partidas {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('='*25)
print(jogador)
print('='*25)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('='*25)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas ')
for i, v in enumerate(jogador['gols']):
    print(f'   ==> na partida {i+1}, fez {v} ')
print(f'No total marcou {jogador["total"]}')