# list: lista de varios elementos se puede modificar (se usa corchete)
lista = ["Angel","Duarte",True,34]
lista[0] = "Eduardo"
print(lista)

# tuple: lista de varios elementos pero no se puede modificar un elemento
# a menos que modificque toda la tupla(se usa parentesis)
tupla = ("Angel","Duarte",True,34)
# tupla[0] = "Eduardo" (sale error debido a que la tupla es inmodificable)
print(tupla) 

# set: crear conjunto, no tiene orden fijo y tampoco se puede modificar un elemento
# a menos quemodifique toda el conjunto, tampoco repite valores(se usa llaves)
conjunto = {"Angel","Duarte",True,34,"Duarte"}
print(conjunto)

#dict: crear diccionario, crear una lista de elementos pero en ves de llamar el elemento
# por el numero de ubicación se llamar por el nombre que le dimos
diccionario = {
    'nombre'    : "angel peña",
    'instagram' : "AngelMaster",
    'es_real'   : True,
    'altura'    : 1.77,
    'repetido'  : "AngelMaster"  
}
print(diccionario['instagram'])
# print(diccionario[2]) no se puede imprimir debido a que es un conjunto y no tiene orden
print(diccionario["altura"] + 2)