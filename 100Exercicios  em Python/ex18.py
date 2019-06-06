''' import math
ang = float(input('Digite o ângulo que voce deseja ? '))
seno = math.sin(math.radians(ang))
print('O ângulo do {} e seno {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo do {} tem o cosseno de {:.2f} '.format(ang, cosseno))
tang = math.tan(math.radians(ang))
print('O ãngulo {} em tangente é {:.2f}'.format(ang, tang))'''

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que voce deseja ? '))
seno = sin(radians(ang))
print('O ângulo do {} e seno {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O ângulo do {} tem o cosseno de {:.2f} '.format(ang, cosseno))
tang = tan(radians(ang))
print('O ãngulo {} em tangente é {:.2f}'.format(ang, tang))