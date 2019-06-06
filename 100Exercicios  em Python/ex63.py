print('='*20)
print('Sequancia de fibonacci')
print('='*20)
n = int(input('Quantos termor voce quer contar '))
te1 = 0
te2 = 1
cont = 3
print('{} -> {}'.format(te1, te2), end='')
while cont <= n:
    t3 = te1 + te2
    print('-> {}'.format(t3), end='')
    te1 = te2
    te2 = t3
    cont += 1
print('-> Fim')
