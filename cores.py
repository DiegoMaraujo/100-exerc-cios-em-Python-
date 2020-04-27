from time import sleep

#função global das cores
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42',
     '\033[0;30;43',
     '\033[0;30;44',
     '\033[0;30;45',
     '\033[7;30m'
    )

#Função dos comandos de ajuda(Help)
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0],end='')
    sleep(2)

#função dos titulos personalizados
def titulo(msg, cor=0):
    tam = len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f' {msg}')
    print('~'* tam)
    print(c[0], end='')
    sleep(1)
#programa
comando = ''
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando =str(input("Função ou biblioteca >"))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo',1)
