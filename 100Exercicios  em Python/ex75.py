num = (int(input('Digite um numero : ')),
int(input('Digite um numero : ')),
int(input('Digite um numero : ')),
int(input('Digite um numero : ')))
print(f'Voce digito os numeros {num}')
if 9 in num:
    print(f'O numero nove aparece {num.count(9)}')
else:
    print('O numero 9 não Foi digitado ')
if 3 in num:
    print(f'o numero 3 aparece na posição {num.index(3)+1}')
else:
    print('O numero 3 não foi digitado')

print('os numeros pares são ')
for n in num:
    if n % 2 == 0:
        print(n , end='')