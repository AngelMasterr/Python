# Escribir un programa que calcule la seride de fibonacci hasta un numero determinado

def serie_fibonacci(dato):
    a = 0
    b = 1    
    serie = [0]
    while b <= dato:        # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34      
        serie.append(b)  
        a, b = b, a + b     # Si las variables van en una sola linea, permite sumar la variable antes que la actualice a su nuevo valor                
    return serie

dato = int(input("Introduzca un numero mayor a 0: "))
print(serie_fibonacci(dato))

# Cree una funcion ára calcular primos lo mas corta psoible con los conocimientos aprendidos

primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, x)), range(2, num+1)))
print(primos_hasta(dato))

# Escribir una lista con todos los numeros primos encontrados hasta el numero dado, usando el metodo Crivo de Eratóstenes
# 1. Crea una lista de números enteros desde 2 hasta el número dado.
# 2. Toma el primer número de la lista como el primer número primo encontrado, y tacha todos sus múltiplos de la lista.
# 3. Toma el siguiente número en la lista que no ha sido tachado como el siguiente número primo, y tacha todos sus múltiplos.
# 4. Repite los pasos 3 hasta que la lista esté vacía o no queden números sin tachar.

def metodo_crivo(dato):
    lista_numeros = list(range(2, dato+1))  
    for n in lista_numeros[+0:]:        
        lista_multiplos_n = list(filter(lambda x: x%n == 0, lista_numeros))    
    
        for num in lista_multiplos_n[1:]:
            if num in lista_numeros:
                lista_numeros.remove(num)
    return lista_numeros
    
print(metodo_crivo(dato))


