# Iterar en diccionarios con for
diccionario = {
    "nombre"    : "angel",
    "apellido"  : "duarte",
    "subs"      : 20000,
    "estado"    : "soltero"   
}

# solo muestra el nombnre de los items pero no el valor de cada uno
for key in diccionario:
    print(key)

# Recorrer diccionar con  los items y sus valores
# items: muestra el item y su respectivo valor como una tupla o lista, es parcedio a "enumerate"
for key in diccionario.items():
    item = key[0]
    valor = key[1]
    print(f"El item es {item} y el valor es {valor}")