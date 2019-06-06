from  random import shuffle
n1 = str(input('Digite o primeiro aluno ? '))
n2 = str(input('Digite o segundo aluno  ? '))
n3 = str(input('Digite o terceiro aluno ? '))
n4 = str(input('Digite o quato aluno ? '))
list = [n1, n2, n3, n4]
shuffle(list)
print('A orden dos sorteados foi ')
print(list)
