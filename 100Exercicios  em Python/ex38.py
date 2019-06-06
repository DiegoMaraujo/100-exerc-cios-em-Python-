nu1 = int(input('Digite o primeiro numero ?'))
nu2 = int(input('Digite o segundo numero ?'))
if nu1 > nu2:
    print('o primeiro {} numero é maior {} '.format(nu1,nu2))
elif nu2 < nu1:
    print('o segundo {} numero é maior {} '.format(nu2,nu1))
elif nu1 == nu2:
    print('esse numeros é igauis')
