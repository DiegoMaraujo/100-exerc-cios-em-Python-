no = str(input('Digite seu nome completo ? ')).strip()
nome = no.split()
print('Seu primeiro no é {} '.format(nome[0]))
print('Seu utimo nome é {}'.format(nome[len(nome)-1]))