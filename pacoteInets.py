from exModulo.Pacotes import pacote
from exModulo.Pacotes import dado

'''p = float(input('Digite o preço: R$ '))
pacote.resumo(p, 20, 12)'''

pe = dado.leiaDinhero('Digite o preco: R$')
pacote.resumo(pe,40,20)

c = dado.leiaInt('digite o preço: R$')
pacote.resumo(c, 40 , 20)
