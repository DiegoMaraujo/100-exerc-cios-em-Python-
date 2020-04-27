def ficha(jog ='<desconhecido>', gol=0):
    print(f'O jogador{jog} fez {gol} gol(s) no Campeonato')


#programa
n = str(input("Nome do jogador"))
g = str(input("Numeros de gols"))
 
if g.isnumeric():#ver se é um numero
    g=int(g)
else:
    g = 0
if n.strip() == '':#tira os espaços
    ficha(gol=g)
else:
    ficha(n,g)
