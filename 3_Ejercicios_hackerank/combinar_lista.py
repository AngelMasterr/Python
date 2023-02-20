# La combinación es una selección no ordenada de objetos. Se utiliza para calcular el número de formas en que se 
# pueden seleccionar un subconjunto de objetos de un conjunto más grande
# crear todas la combinaciones posibles de una cadena en forma ordenada alfabeticamente hasta un entero k
# es decir empezar hacer las combinaciones con K=1 hasta el k introducido

from itertools import combinations

string, k = input("introduzca una palabra a combinar y luego el numero de rango: ").split()
k = int(k)
string = sorted(string)
for i in range (1, k+1):
    combinacion = list(combinations(string, i))
    comb_str = list("".join(i) for i in combinacion)
    for com in comb_str: print(com)

"""from itertools import combinations

s, n = input().split()
s, n = sorted(s), int(n)
print(*(''.join(x) for k in range(n) for x in combinations(s, k + 1)), sep='\n')"""