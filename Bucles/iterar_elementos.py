# Esto sirve apra iterar listas, tuplas y conuntos
# Crear una lista
animales = ["gato", "perro", "loro", "mono", "buho", "leon"]
numeros = [1, 5, 7, 9, 11, 13]

# recorrer la lista de animales
for animal in animales:
    print(f"el animal es: {animal}")

# recorrer y multiplicar los numeros de la lista por 3
for num in numeros:
    mult = num * 3
    print(f"la multiplicación por tres es: {mult}")

# range: iterar numero con la funcion range
for numer in range(3,11):
    print(f"la secuencia de 3 a 10: {numer}")

# Recorrer dos listas de elementos deben ser del mismo tamaño 
for animal, num in zip(animales, numeros):
    print(f"lista 1 el animal es: {animal}")
    print(f"lista 2 el nunmero es: {num}")
    
# Otra manera es la clasica recorrer toda la lista por su indice, "len" es para contar los elementos de la lista
for i in range(len(numeros)):
    print(numeros[i])
  
# La forma correcta de recoorer la lista por su indice  
# enumaerate : da como respuesta una pareja de datos por elemento (tupla), el primero [0]: la posicion y el segundo [1]: el valor
for i in enumerate(numeros):
    posicion = i[0]
    valor = i[1]
    print(f"la posición es {posicion} y el valor es {valor}")
    
# Usando el else en el for, siempre se van a ejecutar
for num in numeros:
    print(num)
else:
    print("Se termino el bucle de for perro")