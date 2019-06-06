resp = 'S'

soma = media = quant= maior = menor = 0
while resp in 'Ss':
    n = float(input('Digite um numero '))
    soma += n
    quant += 1
    if quant == 1:
       maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('quer continua [S/N] ')).strip().upper()[0]
media = soma / quant
print('Voce digito valor {} a media {}'.format(quant, media))
print('O menor numero {} maior numero foi {}'.format(menor, maior))
