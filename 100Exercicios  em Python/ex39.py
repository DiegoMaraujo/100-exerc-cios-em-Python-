from datetime import date # ano atual
atual = date.today().year
nasc = int(input('em qual ano voce naceu ? '))
idade = atual - nasc
print('quem nasceu em {}  tem {} anos  em  {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que ser alistar ')
elif idade < 18:
    saldo = 18 - idade
    print('ainda falta {} anos  para voce se alistar'.format(saldo))
    ano = atual + saldo
    print('seu  alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('voce passo a {} anos   para o alistar'.format(saldo))
    ano = atual - saldo
    print('seu ano de alistamento foi em {}'.format(ano))
