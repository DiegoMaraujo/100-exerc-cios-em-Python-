from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor '))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I] ? ')).strip().upper()[0]
    print(f'Voce jogo {jogador} e o computador {comp} o total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu ')
            v += 1
        else:
            print('voce perdeu ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu ')
        else:
            print('voce perdeu ')
            break
    print('Vamos jogar novamente ')
print('GAME OVER!!!!')