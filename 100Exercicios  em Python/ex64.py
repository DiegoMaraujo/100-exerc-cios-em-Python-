'''n = 0
cont = 0
soma = 0'''

n = cont = soma = 0
n = int(input('Digite um numero [999 para parar] '))
while n != 999:
    if n == 999:
        tot = False
    soma += n
    cont += 1
    n = int(input('Digite um numero [999 para parar] '))
print('O valor {} e a soma foi {}'.format(cont, soma))
