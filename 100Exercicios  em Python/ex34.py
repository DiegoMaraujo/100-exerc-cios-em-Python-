sal = float(input('Qual seu salario ? '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('voce que ganhava {:.2f}R$ começa a ganha  {:.2f} R$'.format(sal, novo))


