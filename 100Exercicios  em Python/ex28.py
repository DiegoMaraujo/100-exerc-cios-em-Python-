from random import randint
from time import sleep
computer = randint(0, 10)
num = int(input('Escolha um numero 0 a 10 ? '))
print('Processando ')
sleep(3)
print(' O numero  sorteado foi {}'.format(computer))
if num == computer:
    print(' parabens voce acerto o numero sorteado {} '.format(computer))
else:
    print('Voce erro o numero sorteado é {} não {} '.format(computer, num))
