nu = int(input('Digite um numero inteiro ?'))
print('''Escolha a conversão:
[1] para binario
[2] para octal
[3] para hexadecimal''')
opcao = int(input('sua opção'))
if opcao == 1:
    print('{} esse numero convertido para binario  {}'.format(nu, bin(nu)[2:]))
elif opcao == 2:
    print('{} esse numero converdido para octal {}'.format(nu, oct(nu)[2:]))
elif opcao == 3:
    print('{} esse numero converdido para hexadecimal {}'.format(nu, hex(nu)[2:]))
else:
    print('opção invalida : tente novamente ')



