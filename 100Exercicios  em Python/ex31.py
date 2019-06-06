from datetime import date
ano = int(input('Que ano quer analisar ? Coloque para analisar o ano atual ? '))
if ano == 0 :
    ano = date.today().year
if ano % 4 == 0 and 100 != 0 or ano % 400 == 0:
    print('Esse ano {} é bisexto '.format(ano))
else:
    print('Esse ano {} não é bisexto '.format(ano))