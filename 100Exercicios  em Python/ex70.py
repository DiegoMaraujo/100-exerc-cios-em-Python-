print(' LOJÃO DE PRODUTOS ')
print('-'*30)
totcomp =  preco = totmil = preco = 0
barato = ''
while True:
    pro = str(input('Nome do produto : '))
    cust = float(input('Valor do produto R$ '))
    preco += 1
    totcomp = totcomp + cust
    if cust >= 1000:
        totmil += 1
    if preco == 1 or cust < menor:
        menor = cust
        barato = pro
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
         break

print(f'O custo total da compra foi R$ {totcomp:.2f}')
print(f' Total de Produtos  acima de R$ 1000  foi  {totmil}')
print(f'O Produto mais barato   foi {barato} que custa R${menor} ')
