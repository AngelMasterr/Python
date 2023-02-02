# Son las fuinciones que viene incorporada en Python, ej:(len, type, print, etc)

# max: Encontrar el número mayor de una lista, dupla y conjutno (debe ser un numero)
numeros = [7, 15, 8, 12, 5.4, 27]
numero_mayor = max(numeros)
print(f"numero mas alto de la lista de numeros es: {numero_mayor}")

# min: Encontrar el número menos de una lista, dupla y conjutno  (debe ser un numero)
numeros = [7, 15, 8, 12, 5.4, 27]
numero_menor = min(numeros)
print(f"numero mas bajo de la lista de numeros es: {numero_menor}")

# round: redondear un numero a una cantidad de decimales
numero_2 = 7.25698412
print(round(numero_2,2))    #redondea el numero a solo dos decimale

# bool: si el resultado es: 0, vacio, False, None ó ninguno (osea que no le pasemos nada) = False 
resultado_1 = bool(0)
resultado_2 = bool()
resultado_3 = bool(False)
resultado_4 = bool([])
print(f"Resultados bool sin valor: {resultado_1, resultado_2, resultado_3, resultado_4}")  

# bool: si el resultado es un elemento con valor devuelve = True 
resultado_5 = bool(15.2,)
resultado_6 = bool(-7)
resultado_7 = bool(True)
resultado_8 = bool([0, None, False, []]) #Aunrque dentro de la lista todos lo valores son nulos, no analiza su contenido, asume que la lista tiene valor
print(f"Resultados bool con valor: {resultado_5, resultado_6, resultado_7, resultado_8}")

# all: retorna True si todos los elementos de la lista, tupla o conjunto tienen valor (igual que bool, pero si analiza listas,tuplas o conjuntos)
resultado_all1 = all([15, True, [2,3], -7])     #True
resultado_all2 = all([32, [7,3], -12.3, True])  #True
resultado_all3 = all([32, [7,3], 0, True])      #False
resultado_all4 = all([32, [7,3], None, True])   #False
print (f"Resultados all las dos ultima contienen algun dato de la lista sin valor: {resultado_all1,  resultado_all2, resultado_all3, resultado_all4}")

# sum: sumar todos los numero de una secuencia (lista, dupla, conjunto) 
lista_num = [1,2,3,4,5]
print(sum(lista_num))




