print('='*23)
print('Progresão aritimetica ')
print('='*23)
num = int(input(' primeiro termo '))
razao = int(input(' razão '))
decimo = num + (10-1) * razao #formula do enesimo termo da pa
for c in range(num, decimo + razao, razao):
    print(' {} '.format(c), end='->')
print(' acabo ')
