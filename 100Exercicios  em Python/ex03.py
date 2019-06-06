a = input('digite algo ')
print('o tipo primitivo é {} '.format(a), type(a))
print('so tem espaço ? {}'.format(a), a.isspace())
print('é um numero ? {}'.format(a), a.isnumeric())
print('é alfabetica ?{}'.format(a), a.isalpha())
print('é alfa numerico ? {}', a.isalnum())
print('esta em letras maiscula ? {}'.format(a), a.isupper())
print('esta em misnucula ? {} '.format(a), a.islower())
print('esta capitalizada?  {} '.format(a), a.istitle())


