# Creando una funcion simple
def saludar():
    print("hola angel, eres mágnifico")    
    
saludar()   # ejecuta la funciom simple 


# Crear una función con un parametro (variable)
def saludar(nombre):
    print(f"hola {nombre}, eres lo máximo")
    
saludar("eduardo")  # ejecuta la funcion con el valor del parametro "nombre" 


# Crear una funcion con varias parametros
# Saludar si es hombre, mujer o no se define
sexo = "sdsds"
def saludar(nombre, sexo):    
    sexo = str(sexo)    # si llegara a ser un numero lo convierte a string y no da error    
    sexo = sexo.lower() # convierte todas las letras a minuscula
    if sexo == "hombre":
        print(f"{nombre}, eres el {sexo} mas inteligente que existe en el planeta")
    elif sexo == "mujer":
        print(f"{nombre}, eres la {sexo} mas hermosa del universo")
    else:
        print(f"{nombre}, eres una persona increible")

saludar("angel", "hombre")
saludar("camila", "mujer")
saludar("jorge", "ni idea")
saludar(45, 56)


# Crear una funcion que detecte si el numero es primo (debe ser mayor que 1)
def calcula_primo(numero):
    if numero > 1:        
        for num in range(2,numero):
            if numero % num == 0:   # modulo: multiplica "num" la cantidad de veces necesarias para acercarce a "numero" y da resultado lo que falta
                print(f"{numero} No es primo")
                break
        else:
            print(f"{numero} Es primo")
    else: print("El numero debe ser mayor que 1 pelotudo")

num_primo = int(input("Introduza un numero para saber si es primo: "))
calcula_primo(num_primo)


# Crear una funcion que cuente el numero de caracteres de la variable, pero sin mostrarla (return: es indispensabel para guardar el valor)
def numero_caracteres (valor):
    valor = str(valor)
    cantidad = len(valor)
    return cantidad, valor  # return: es indispensable para guardar el valor, lo guarda como una dupla si hay mas de un valor

dato = input(f"Introduza un nombre o numero: ")
Caracteres = numero_caracteres(dato)
print(f"la cantidad de Caracteres que tiene {Caracteres[1]} es {Caracteres[0]}")


# Forma optima para sumar numero de una lista
def sumar(numeros):
    sum_num = sum(numeros)
    return sum_num

resultado = sumar([1, 2, 3, 4, 5]) # Es necesario pasar los argumentos como un lista o tupla
print(f"la suma es: {resultado}")


# Forma optima para sumar numeros de sin tenerlos en una lista (args / *): convierte los argumentos a una dupla
def sumar(*numeros):    # *: Estoy diciendo que todos los argumentos de la variable numeros los convierta en dupla
    sum_num = sum(numeros)
    return sum_num

resultado = sumar(1, 2, 3, 4, 5) # Ya no es necesario pasar los argumentos como un lista o tupla, debido que se especifica con (args / *)
print(f"la suma es: {resultado}")


