frase = str(input('Digite uma frase ? ')).upper().strip()
print('A letra a aparece ? {} '.format(frase.count('A')))
print('A letra a aparece na posição {} ? '.format(frase.find('A')+1))
print('A utima letra a aparece na posição {} ? '.format(frase.rfind('A')-1))
