def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior']= max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['sitauação'] = 'Ruim'
    return r

def numero():
    for re in range(3):
        re = float(input('digite a nota'))
    return re


resp = notas(numero(), sit=True)
print(resp)
