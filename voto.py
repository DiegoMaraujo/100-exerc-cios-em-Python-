#função do programa
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com{idade} anos : Não Vota'
    elif 16 <= idade >= 18 or idade > 65:
        return f'com {idade} anos:Voto opcional'
    else:
        return f'Com{idade} anos: voto obrigatorio'

nasc= int(input("Em que ano voce nasceu?"))
print(voto(nasc))



