# lambda: Crea funciones anonimas, son funciones basicas y rapidas
Multiplicar_por_dos = lambda x : x*2
print(Multiplicar_por_dos(7))


numeros = [1,2,3,4,5,6,7,8,9,20,21,22,23] 

# Crear una funcion que cree una lista con solo numeros pares de la lista "numeros" (manera larga)
numeros_pares = list()
def num_pares(aaa):
    for num in aaa:
        if num % 2 == 0:
            numeros_pares.append(num)
    return numeros_pares
print(num_pares(numeros))


# Crea otra funcion que muestre los numero pares pero iterando desde afuera usando filter (manera medio larga)
def num_pares_2(bbb):
    if bbb % 2 == 0:
        return True        
# filter: se introducen dos parametros (la funcion y la lista a analizar) analiza cada valor de la lista (parecido a for)
numeros_pares_2 = filter(num_pares_2, numeros) # filtra uno por uno los valores de la lista (parecido a for)
print (list(numeros_pares_2))   # Es necesario indicar que es una lista para darle forma a todos los valores guardados


# Crea otra funcion que muestre los numero pares pero de manera corta con (lambda y filter)

numeros_pares_3 = filter (lambda num : num % 2 == 0, numeros)   # lambda: si cumpla la condicion retorna True y guarda el valor
print(list(numeros_pares_3))                                    # filter: analiza cada valor de la lista de "numeros"

# map: es parecido a filter, pero en ves de filtrar regresa todos los valores cumplan o no la función
# todo los valores introducido deben ser numero separados por espacio, gracias a "map" los convierte en enteros
integer_list = map(int, input().split()) 