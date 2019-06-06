medida = float(input('Digite uma distancia em metros '))
cm = medida * 100
mm = medida * 1000
kl = medida / 1000
hm = medida / 100
da = medida / 10
dc = medida * 0.1


print('As medidas de {} \n  em metros é {} \n  e em centimetros é {}\n e de kilometro {}\n e de hectômetro {}\n e decametro {}\n e decimetro {}'.format(medida, mm, cm, kl, hm, da, dc))
