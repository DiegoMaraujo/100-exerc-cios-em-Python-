vel = float(input('Qual velocidade voce esta diriginto ? '))
if vel > 80:
    print(' multado! voce exeteu a velocidade 80km/h {}km/h '.format(vel))
    mult = (vel - 80) * 7
    print('Voce foi multado em {:.2f} R$ '.format(mult))
print('Tenha uma boa viaje ')
