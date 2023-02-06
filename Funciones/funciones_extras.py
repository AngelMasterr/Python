# crear una funcion simple con varios valores
def persona(nombre, apellido, adjetivo):
    return(f"{nombre} {apellido} eres una persona muy {adjetivo}")

# Introduir 3 valores distintos con un solo input (split: separa la frase por cada espacio y le asiga el valor a cada variable)
nombre, apellido, adjetivo = input("introduzca tu nombre, apellido y adjetivo separados por espacio: ").split()
print(persona(nombre, apellido, adjetivo))

