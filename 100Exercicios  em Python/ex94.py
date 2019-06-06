galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo F/M ')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Erro ! por favor digite M ou F ')
    pessoa['idade'] = int(input('idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO ! digite S ou N ')
    if r == 'N':
        break
print('='*40)
print(f'O todol temos {len(galera)} pessoas cadatradas  ')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos ')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} {v}; ', end='')
        print()
print('   <<<< FIM >>>>  ')


