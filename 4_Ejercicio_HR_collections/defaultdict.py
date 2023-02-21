# defaultdict una subclase de dict de collections en Python que proporciona una manera conveniente de definir 
# un valor predeterminado para cualquier nueva clave que se agregue al diccionario

# Introducir dos enteros n y m, crear la lista_a con n letras y lista_b con m letras de letras, la tarea es recorrer 
# la lista_b # letra por letra y ubicar las posciones donde se encuentre en la lista_a
"""
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b"""
d = defaultdict(list)
n, m = map(int, input().split())
group_a = []; group_b = []
for i in range(n): group_a.append(input())
for i in range(m): group_b.append(input())

for j in group_b:
    for i in range(len(group_a)):
        if j == group_a[i]:
            d[j].append(i+1)
        elif j not in group_a: 
            d[j].append(-1)
for i in d.values(): print(*i)
"""
from collections import defaultdict
d = defaultdict(list)
n,m = map(int,input().split())
for i in range(n):
    d[input()].append(str(i+1))
#print(d['a'])
#print(d['b'])
for j in range(m):
    print(' '.join(d[input()]) or -1)"""
    