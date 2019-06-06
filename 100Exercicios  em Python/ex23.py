'''num = int(input('Informe um numero ?'))
n = str(num)
print('Analisando o Numero {} '.format(num))
print(' unidade {} '.format(n[3]))
print(' centena {} '.format(n[2]))
print(' dezena {} '.format(n[1]))
print(' milhar {} '.format(n[0]))'''

num = int(input('Informe um numero ?'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o Numero {} '.format(num))
print(' unidade {} '.format(u))
print(' centena {} '.format(d))
print(' dezena {} '.format(c))
print(' milhar {} '.format(m))