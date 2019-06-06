jogador = dict()
partidas = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quandos jogos {jogador["nome"]} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quandos Gols marco na partida {c+1} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar [S/N]')).upper()[0]
        if r in 'SN':
            break
        print('ERRO ! Digite S ou N')
    if r == 'N':
        break
print('-'*30)
for i in jogador.keys():
    print(f'{i:<12}', end='')
print('')
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>2}', end='')
    for d in v.values():
        print(f'{str(d):<12}', end='')
    print()
print('-'*30)
while True:
    op = int(input('Quer ver os dados d qual jogado digite [999 para parar]'))
    if op == 999:
        break
    if op >= len(time):
        print(f'Não existe jogador com essa opeção: ')
    else:
        print(f' --Levandamento do jogador {time[op]["nome"]} -- ')
        for i, g in enumerate(time[op]['gols']):
            print(f'  no jogo {i+1:>2} fez {g:>2} gols ')
    print('<<<<<<<<<<<     FIM    >>>>>>>>>>>>>>')


