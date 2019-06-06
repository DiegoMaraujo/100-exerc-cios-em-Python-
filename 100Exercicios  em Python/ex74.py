from random import randint

numeros = (randint(1, 5), randint(1, 5), randint(1, 5),
           randint(1, 5), randint(1, 5))

print('Os numeros Sorteados foi ', end='')

for n in numeros:
    print(f'{n}', end='',)

print(f'\n O maior numero sorteado foi {max(numeros)}')
print(f'O menor numero sorteado foi {min(numeros)}')