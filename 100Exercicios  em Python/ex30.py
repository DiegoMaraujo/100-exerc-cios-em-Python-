'''dist = float(input('Qua a distancia da viaje ? '))
print('Voce esta preste a começar a viajem  de {} Km'.format(dist))
if dist <= 200:
  preco = dist * 0.50
else:
   preco = dist * 0.45
print('O valor da viaje é {:.2f} R$'.format(preco))'''

dist = float(input('Qua a distancia da viaje ? '))
print('Voce esta preste a começar a viajem  de {} Km'.format(dist))
preco = dist * 0.50 if dist <= 200 else dist * 45 # infe lin ou operador simplificado
print('O valor da viaje é {:.2f} R$'.format(preco))
