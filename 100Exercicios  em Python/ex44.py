print('='*10,'compras ','='*10)
preco = float(input('Digite o valor das compras R$ ? '))
print('''Formas de pagamentos
opção [1] á vista dinheiro /cheque
opçao [2] á vista cartão 
opção [3] 2x no cartão 
opção [4] 3x ou mais x no cartão''')
op = int(input('qual a  opção '))
if op == 1:
    total = preco - (preco * 10 / 100)
elif op == 2 :
    total = preco - (preco * 5 / 100)
elif op == 3:
    total = preco
    par = preco / 2
    print('o valor da sua compra em 2x é {} R$'.format(par))
elif op == 4:
    total = preco + (preco * 20 / 100)
    totalpar = int(input('Quantas parcelas '))
    parcela = total / totalpar
    print('Sua compra sera parcelatas {}x de R${:.2f} com juros '.format(totalpar, parcela))
print('Sua compra de {} R$ custar no final {} R$ '.format(preco, total))





