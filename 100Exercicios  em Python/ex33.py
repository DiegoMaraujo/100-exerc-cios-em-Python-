a = int(input('Digite 1 numero ? '))
b = int(input('Digite  2 numero ? '))
c = int(input('Digite  3 numero ? '))
# verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero é {}'.format(maior))
print('O menor valor foi {}'.format(menor))
