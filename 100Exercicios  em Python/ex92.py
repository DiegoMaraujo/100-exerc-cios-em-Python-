from datetime import datetime
traba = dict()
traba['nome'] = str(input('Nome: '))
nsc = int(input('Ano de nascimento '))
traba['idade'] = datetime.now().year - nsc
traba['ctps'] = int(input('Ano de carteira de trabalho (o não tem ): '))
if traba['ctps'] != 0:
    traba['contratacao'] = int(input('Ano de contratação '))
    traba['salario'] = float(input('Valor do salario R$'))
    traba['aponsentadoria'] = traba['idade'] + ((traba['contratacao'] + 35) - datetime.now().year)
print('-'*25)
for k, v in traba.items():
    print(f'{k} tem o valor {v}')