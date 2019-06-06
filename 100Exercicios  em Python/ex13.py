salario = float(input('Qual o salario do funcionario R$ '))
novosal = salario + (salario * 15 / 100)
print('O salario do funcionario {:.2f} R$ com 15% de aumento é {:.2f}'.format(salario, novosal))
