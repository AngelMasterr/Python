diccionario = {
    "nombre"    : "Angel",
    "apellido"  : "Duarte",
    "subs"      : 10000,
    "cabello"   : "dorado"
}

# muestra todos los items que contiene el diccionario (dict)
claves = diccionario.keys() 
print(claves)

# busca el item en el diccionario, si no lo encuentra sale error
buscar = diccionario["nombre"] 

# get : es necesario para que no salga error cuando no encuentra el item en el diccionario y da como resultado "none"
buscar = diccionario.get("nombre") 
print(buscar)

# pop : elimina un item del diccionario
eliminar = diccionario.pop("apellido")
print(diccionario)

# items : itera cada item con su significado en un vector
iterable = diccionario.items()
print(iterable)

# clear : elimina todos los item del diccionario
eliminar_todo = diccionario.clear()
print(diccionario)
