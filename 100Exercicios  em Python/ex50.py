soma = 0
cont = 0
for c in range(1, 501, 2): #pulando de 2 em dois vai mostra os numeros impares
    if c % 3 == 0: # numeros divisivio por  3
        cont = cont + 1 # cont += 1 /soma todos os numeros divisivel por 3
        soma = soma + c #soma += c / soma de todos os numero impares
print('A soma de todos os {} valores  solicidados é {}'.format(cont, soma))

