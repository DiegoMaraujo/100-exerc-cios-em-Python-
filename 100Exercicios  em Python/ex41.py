from datetime import date
anoatual = date.today().year
nasc = int(input('Em que ano voce nasceu ? '))
ano = anoatual - nasc
print('O atleta tem {} anos'.format(ano))
if ano <= 9:
    print('Atleta mirim')
elif ano <= 14:
    print('Atleta infatil')
elif ano <= 19:
    print('Atleta junior')
elif ano <= 25:
    print('Atleta sênior')
else:
    print('Atleta master')