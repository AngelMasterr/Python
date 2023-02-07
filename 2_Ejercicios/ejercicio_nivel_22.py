# Crear una funcion que al introducir un numero, genere todos los numeros primos hasta llegar al numero dado

def numeros_primos(aaa):                        # aaa = 5
    if aaa > 1:
        lista_num = list(range(2, aaa+1))       # 2, 3, 4, 5
        tamaño = len(lista_num)                 # 4
        lista_primos = []                       # lista vacia
        for num in range(tamaño):               # recorrer todo el vector desde 0 hasta 3 (4 posiciones)
            for dat in range(2, lista_num[num]):
                if lista_num[num] % dat == 0:   # el numero no es primo
                    break                
            else: lista_primos.append(lista_num[num])            
        return lista_primos
                        
    else: print("el numero debe ser mayor a 1 pelotudo")

dato = int(input("Introduzca un nuemro mayor a 1: "))
primos = numeros_primos(dato)
print(primos)


# Es mejor crear dos funciones y se ahorra tanto mierdero que ni se entiende (aclaro que lo hice con el conocimiento que tenia)

# Verificar si el numero es primo
def numeros_primos_2(bbb):
    for num in range(2, bbb):
        if bbb % num == 0:
            return False
    return True                # si es primo retorna True

# verificar la lista de numeros si son hasta el numero introducido
def lista_numeros_primos(ccc):
    lista_primos = []
    for num in range(2, ccc+1):
        if numeros_primos_2(num) == True:
            lista_primos.append(num)
    return lista_primos

dato = int(input("Introduzca un numero mayor a uno: "))
if dato > 1:
    print(lista_numeros_primos(dato))
else:
    print("El numero debe ser mayor a 1")
    
        
    


