# list : funcion para crear una lista
lista = list(["hola", "angel", "eduardo", 34, 1.78])
print(lista)

# len : funcion que deveulve la cantidad de elementos de una lista 
print(len(lista))

# append : metodo para agregar un elemento a una lista, primero lo agrega y luego lo llama (dos lineas)
lista.append("soltero")
print(lista) 

# insert : metodo para agregar un elemento a una lista en la posición dada
lista.insert(1,"mi bello")
print(lista) 

# extend : metodo para agregar varios elementos a una lista 
lista.extend(["soy rico","colombiano"])
print(lista) 

# pop : metodo para eliminar un elemento de una lista en la posición dada
lista.pop(2) # elimina el tercer elemento
lista.pop(-1) # (-1) elimina el ultimo elemento, (-2) elimina el penultimo, etc.
print(lista) 

# remove : metodo para eliminar un elemento de una lista segun el dato dado
lista.remove(1.78) # si no esta el dato exacto no lo elimina
print(lista) 

# sort : metodo que ordena los elementos de forma ascendente, (enteros) 
lista_2 = list([8,2,6,9,4,3,1,5,0])
lista_2.sort()
print(lista_2)

lista_2.sort(reverse=True) # reverse=True ; cambiar el orden a descendente
print(lista_2)

# reverse : cambia el orden de una cadena de atras hacia delante
lista.reverse()
lista_2.reverse()
print(lista)
print(lista_2)

# index() : busca la posicion de un dato en una lista, si no la encunetra devuelve una excepcion (error)
print(lista_2.index(3))
