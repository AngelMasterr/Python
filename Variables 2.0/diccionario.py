# crenado diccionario con dict
diccionario_1 = dict(nombre="angel", apellido="duarte")

# creando diccionario con llaves
diccionario_2 = {
    "nombre" : "angel",
    "apellido" : "duarte"
}
print(type(diccionario_1))
print(type(diccionario_2))

# fromkeys: Poder crear un diccionario solo con items sin el significado (da como repsuesta "none" por cada item)
diccionario_3 = dict.fromkeys(["nombre","apellido","edad"]) # es necesario que este entre corchetes, si solo esta entre parentesis iterara letra por letra
print(diccionario_3)    

diccionario_4 = dict.fromkeys(["nombre","apellido","edad"], "paz") # igual que antes pero en ves de dar el valor de "none" a cada item da el valor de "paz"
print(diccionario_4)