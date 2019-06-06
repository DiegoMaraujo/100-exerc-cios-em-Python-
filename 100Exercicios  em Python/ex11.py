lar = float(input('Largura da parede '))
alt = float(input('Altura da parede '))
are = lar * alt
print('A sua parede tem {} x {} em área {} m²'.format(lar, alt, are))
tin = are / 2
print('A para pinta a {} m² é ncessario {} litros de tinta '.format(are, tin))