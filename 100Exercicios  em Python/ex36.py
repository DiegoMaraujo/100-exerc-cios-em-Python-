casa = float(input('Qual o valor da casa R$ ? '))
salario = float(input('Qual o valor do salario R$ ? '))
ano = int(input('em quantos ano vai paga ?'))
minimo = (salario * 30) / 100
prestacao = casa / (ano * 12)
print('30% do seu salario é  {:.2f}'.format(minimo))
print('para pagar uma casa R${:.2f} em {} anos a prestação é {:.2f}'.format(casa,ano,prestacao))
if 'o valor da prestacao <= minimo':
    print('esprestimo consedido')
else:
    print('emprestimo negado ')