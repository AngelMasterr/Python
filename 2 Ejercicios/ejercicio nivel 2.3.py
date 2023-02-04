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

