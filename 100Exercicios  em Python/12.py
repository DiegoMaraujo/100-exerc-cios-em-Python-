extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Tente novamente. Digite um número de  [ 0 a 20 ] : '))
    while n < 0 or n > 20:
        n = int(input('Tente novamente. Digite um número de  [ 0 a 20 ] : '))
    print(f'O numero {n} por extenso é {extenso[n]}')
    res = input('Quer continuar? [S/N]: ').upper().strip()[0]
    if res == 'S':
        n = int(input('Digite um número de [ 0 a 20] : '))
    res = ''
    while res not in 'SN':
        res = str(input('Não Entendi sua resposta, Digite novamente [S/N]: ')).upper().strip()[0]
    if res == 'N':
        break
print('Obrigado por usar o programa!')﻿
