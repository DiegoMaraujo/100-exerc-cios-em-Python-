peso = float(input('Qual seu peso (kg) ? '))
altura = float(input('qual sua altura ? '))
imc = peso / (altura ** 2)
print('O imc é {:.1f}'.format(imc))
if imc < 18.5 :
    print('Abaixo do peso ' )
elif imc >= 18.5 and imc < 25: # 18.5 <= imc < 25
    print('Peso ideal')
elif imc <= 25 and imc < 30:
    print('Sobre peso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')