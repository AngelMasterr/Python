my_dict = {'a': 10, 'b': 5, 'c': 15, 'd': 20, 'e': 10}

# Ordenar el diccionario por valor en orden descendente y luego por key en orden ascendente
sorted_dict = sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))

print(sorted_dict)

# Ordena los items de forma descendente por su value y los que se respiten los ordena en forma ascendente por su key
  
# [('d', 20), ('c', 15), ('a', 10), ('e', 10), ('b', 5)]