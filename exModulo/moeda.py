def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res
def diminuir(preco , taxa):
    res = preco - (preco * taxa/100)
    return res

def dobro(preco):
    res = preco * 2
    return res

def metade(preco = 0):
    res = preco /2 
    return res
def moeda(preco = 0, moeda ='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')
#//////////////////////////////////////////////////////////
def aumento(preco=0, taxa =0, formato=False):
    res = preco +(preco* taxa/100)
    return res if formato is False else moeda(res)

def dobra(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def diminui(preco =0 , taxa = 0, formato= False):
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)

def metadi(preco = 0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

#/////////////////////////////////////////////////////////////
def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR '.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro o preço: \t{dobra(preco, True)}')
    print(f'Metade do preço: \t{metadi(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preco, taxaa,True)}')
    print(f'{taxar}% de redução: \t{diminui(preco, taxar, True)}')
    print('-'*30)

