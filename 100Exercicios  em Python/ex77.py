palavras = ('python', 'curso', 'diego', 'etec', 'linguagem', 'gratis', 'indio')
for p in palavras:
    print(f'\n As vogais da palavra  {p} são  ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end='')
