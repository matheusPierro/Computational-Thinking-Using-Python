


from operator import length_hint


def dizNome(nome):
    print(nome)

def soletraNome(nome):
    for contLetra in range(0, length_hint(nome)):
        print(nome[contLetra])

print(soletraNome(dizNome("Thiago")))
