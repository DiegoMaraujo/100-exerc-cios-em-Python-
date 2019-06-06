from time import sleep
valor1 = int(input('Digite o primeiro valor '))
valor2 = int(input('Digite o segundo valor '))
opcao = 0
while opcao != 5:
    print('''
    [1]soma
    [2]mutipliacaçao
    [3]maio valor
    [4]novos numeros
    [5]sair do programa''')
    opcao = int(input('Qual sua opção '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma do {} + {} = {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print('A mutiplicação {} x {} = {}'.format(valor1, valor2, mult))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('entre o {} e o {} o Maior é {}'.format(valor1, valor2, maior))
    elif opcao== 4:
        valor1 = int(input('Primeiro valor '))
        valor2 = int(input('Segundo valor'))
    elif opcao == 5:
        print('Fim do programa')
    else:
        print('Opção invalida')
    print('-*-' * 20)
    sleep(2)
print('fim do programa')



