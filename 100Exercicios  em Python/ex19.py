from random import choice
n1 = str(input(' Digite o 1 aluno ? '))
n2 = str(input(' Digite o 2 aluno ? '))
n3 = str(input(' Digite o 3 aluno ? '))
n4 = str(input(' Digite o 4 aluno ? '))
lista = [n1, n2, n3, n4]
sort = choice(lista)
print(' O aluno sorteado foi {}'.format(sort))




