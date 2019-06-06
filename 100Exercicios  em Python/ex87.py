matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
smp = smcl = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{[l]}{[c]}] '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            smp = smp + matriz[l][c]
    print()

print('*'*30)

print(f'a soma de todos os pares foi {smp}')
for l in range(0, 3):
    smcl = smcl + matriz[l][2]
print(f'A soma dos valores da terceira coluna foi {smcl}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O mairo valor da culona 2 foi {mai}')


