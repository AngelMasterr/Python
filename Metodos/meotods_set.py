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

# add(elemento): Agrega un elemento al conjunto.

# remove(elemento): Elimina un elemento del conjunto. Si el elemento no se encuentra, se lanza un error KeyError.

# discard(elemento): Elimina un elemento del conjunto. Si el elemento no se encuentra, no hace nada y no lanza un error.

# intersection(set2): Devuelve un nuevo conjunto que contiene los elementos comunes entre el conjunto actual y el conjunto set2.

# union(set2): Devuelve un nuevo conjunto que contiene todos los elementos del conjunto actual y del conjunto set2.

# difference(set2): Devuelve un nuevo conjunto que contiene los elementos del conjunto actual que no están en el conjunto set2.

