lista = list()
menor = 0
maior = 0
for l in range(0, 5):
    lista.append(int(input(f'digite um valor:{l} ')))
    if l == 0:
        maior = menor = lista[l]
    else:
        if lista[l] > maior:
            maior = lista[l]
        if lista[l] < menor:
            menor = lista[l]
print('*'*20)
print(f'O maior numero foi {maior} na posição ', end='')
for c, i in enumerate(lista):
    if i == maior:
        print(f' {c}.. ', end='')
print()
print(f'O menor  numero foi {menor} na posição ', end='')
for c, i in enumerate(lista):
    if i == menor:
        print(f' {c}.. ', end='')
print()