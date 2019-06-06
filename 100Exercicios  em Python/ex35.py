print('='*20)
print('Analise se forma um triangulo')
print('='*20)
r1 = float(input('Primeiro seguimento '))
r2 = float(input('Segundo seguimento '))
r3 = float(input('Terceiro seguimento '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2 :
    print('Os seguimentos acima podem forma um triangulo')
else:
    print('Os seguimento não forma um triangulo')
