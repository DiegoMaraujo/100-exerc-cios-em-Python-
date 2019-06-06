from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pes in range(1, 8):
    nasc = int(input('Digite seu ano {} de nacimento '.format(pes)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1

    else:
        totalmenor += 1
print('mairores de idade tem {}'.format(totalmaior))
print('menor de iadade tem {}'.format(totalmenor))
