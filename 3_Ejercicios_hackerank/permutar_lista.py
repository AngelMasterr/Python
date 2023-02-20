# La función permutations es una función del módulo itertools de Python que devuelve todas las posibles 
# permutaciones de un iterable dado 

# itertools.permutations(iterable, r=None) Donde iterable es el objeto iterable del cual se desean generar 
# las permutaciones y r es el número de elementos que se deben seleccionar para formar cada permutación. 

from itertools import permutations

string, k = input("introduzca una palabra y luego el numero a permutar: ").split()
k = int(k)

permutacion = list(permutations(string, k))
perm_string = list("".join(i) for i in permutacion)

orden_string = sorted(perm_string)
for i in orden_string:
    print(i)
