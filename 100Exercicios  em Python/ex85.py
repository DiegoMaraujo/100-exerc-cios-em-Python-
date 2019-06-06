nu = [[], []] # cria lista tretro de uma lista e quarda valores nelas
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c} valor '))
    if valor % 2 == 0:
        nu[0].append(valor)
    else:
        nu[1].append(valor)
print('='*30)
nu[0].sort()# ordena numeros em orde crecente
#nu[1].sort()
print(f'o pares são {nu[0]}')
print(f'os impares são {sorted(nu[1])}') # ordena numeros em ordem crecente
