from random import randint
comput = randint(0, 10)
print('Sou seu computador acabei de persa em um numero')
print('Sera que voce concegue adivinha qual foi o numero ? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ? '))
    palpite += 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('Mais...Tente mais uma vez')
        elif jogador > comput:
            print('Menos...Tente mais uma vez')
print('Acertou com {} palpite'.format(palpite))


