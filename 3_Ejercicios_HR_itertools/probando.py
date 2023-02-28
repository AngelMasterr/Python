import itertools

palabra = "cold"
permutaciones = itertools.permutations(palabra)
anagramas = []

for i in permutaciones:
    print("".join(i))