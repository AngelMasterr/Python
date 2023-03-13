myset = {1, 2} # Directly assigning values to a set
myset = set()  # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
print(myset)
# {'a', 'b'}

myset.add('c')
print(myset)
# {'a', 'c', 'b'}
myset.add('a') # As 'a' already exists in the set, nothing happens
myset.add((5, 4))
print(myset)
# {'a', 'c', 'b', (5, 4)}

myset.update([1, 2, 3, 4]) # update() only works for iterable objects
# myset
# {'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
myset.update({1, 7, 8})
print(myset)
# {'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
myset.update({1, 6}, [5, 13])
print(myset)
# {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}

myset.discard(10)
print(myset)
# {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}
myset.remove(13)
print(myset)
# {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 3}

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
a.intersection(b) # Values which exist in a and b
# {2, 4}
a.difference(b) # Values which exist in a but not in b
# {9, 5}

# ^: diferencia simétrica, y se puede entender como la unión de los conjuntos que no tienen elementos en común.
a ^ b 
# {5, 9, 11, 12}

# add(elemento): Agrega un elemento al conjunto.

# remove(elemento): Elimina un elemento del conjunto. Si el elemento no se encuentra, se lanza un error KeyError.

# discard(elemento): Elimina un elemento del conjunto. Si el elemento no se encuentra, no hace nada y no lanza un error.

# intersection(set2): Devuelve un nuevo conjunto que contiene los elementos comunes entre el conjunto actual y el conjunto set2.

# union(set2): Devuelve un nuevo conjunto que contiene todos los elementos del conjunto actual y del conjunto set2.

# difference(set2): Devuelve un nuevo conjunto que contiene los elementos del conjunto actual que no están en el conjunto set2.

# set_a ^ set_b: ^: diferencia simétrica la unión de los conjuntos que no tienen elementos en común. El resultado será 
# un nuevo conjunto que contiene los elementos que están en uno de los conjuntos, pero no en ambos:
