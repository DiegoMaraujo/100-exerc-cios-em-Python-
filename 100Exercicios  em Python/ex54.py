frase = str(input('Digite uma frase ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]'''
print('o inverso de {} é {}'.format(frase, inverso))
if inverso == junto:
    print('temos um palitrome !')
else:
    print('a frase não é um palitrome ! ')