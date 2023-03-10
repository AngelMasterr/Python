# Dadas dos cadenas a, y b, que pueden ser o no ser de la misma longitud, determinan el número mínimo de eliminaciones 
# de caracteres requeridas para hacer a y b anagramas. Cualquier carácter se puede eliminar de cualquiera de las cadenas.

# subtract(): la función subtract de la clase Counter en Python se utiliza para realizar operaciones de resta entre objetos 
# contadores, actualizando el objeto actual para reflejar los resultados de la operación

from collections import Counter

def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    
    a.subtract(b)
    print(a)
    return sum(map(abs, a.values()))

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

print(makeAnagram(a,b))