maior = 0
menor = 0
for pes in range(1, 6):
    peso = float(input('Digite {} seu peso '.format(pes)))
    if pes == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi {}kg'.format(maior))
print('o menor peso foi {}Kg'.format(menor))



