from itertools import groupby

#numbers = list(map(int, input()))
numbers = input()
groups = groupby(numbers)
list_gro = []
for key, gro in groups:
    item = (len(list(gro)), key)
    list_gro.append(item)
    #print(len("".join(list(gro))), key)
