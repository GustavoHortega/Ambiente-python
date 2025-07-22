#printe as vogais em letras maiúsculas.
tupla = ('Mario','Peaches','Luigi','Yoshi','Kojima','Nefario')

for palavra in tupla:
    print(f'\n Palavra: {palavra.upper()} Vogais:')

    for letra in palavra:
        if letra.lower() in 'aeiou':

            print(letra.upper(), end=' ')