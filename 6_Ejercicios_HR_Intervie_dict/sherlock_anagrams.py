# Dos cadenas son anagramas entre sí si las letras de una cadena se pueden reorganizar para formar la otra
# cadena. Dada una cadena, encuentre el número de pares de subcadenas de la cadena que son anagramas entre sí.
""" 
ejemplo
input = s: "cdcd" --- output = 5
Hay dos pares anagramáticos de longitud 1: [c,c] y [d,d] = [0,2] y [1,3]
Hay tres pares anagramáticos de longitud 2: [cd,dc], [cd,cd],[dc,cd] = [[0,1],[1,2]], [[0,1],[2,3]], [[1,2],[2,3]] 
"""
from collections import Counter
def sherlockAndAnagrams(s):
    # Write your code here
    sub_s = []
    sum_s = 0
    for n in range(1, len(s)):
        for i in range(len(s)-n+1): 
            sub_s.append(s[i:i+n])
        order_s = ["".join(sorted(x)) for x in sub_s]
        dict_s = Counter(order_s)   
    for key, value in dict_s.items():
        comb_s = list(combinations(range(value), 2))
        sum_s += len(comb_s) 
    return sum_s
            