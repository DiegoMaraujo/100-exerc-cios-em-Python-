nome = str(input('Digite seu nome completo ? ')).strip()
print('Analise seu nome ')
print('seu nome com letras maiscula é {} '.format(nome.upper()))
print('seu nome em letras minuscula é {} '.format(nome.lower()))
print('se nome completo  tem {} letras '.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('seu  primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
