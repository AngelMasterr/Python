# all() es una función integrada de Python que toma un iterable como argumento y devuelve True si todos 
# los elementos en el iterable son verdaderos, es decir, si todos los elementos son diferentes de cero, 
# vacío o None. De lo contrario, devuelve False.
# Por ejemplo: Verificar si todos los elementos de una lista son mayores que 0
lista2 = [2, 4, 6, 0, 8]
if all(x > 0 for x in lista2):
    print("Todos los elementos de la lista son mayores que 0")
else:
    print("Al menos un elemento de la lista es menor o igual a 0")

# any(): Devuelve True si al menos uno de los elementos de la secuencia satisface una condición determinada.
# Por ejemplo:
lista = [1, 2, 3, 4, 5]
if any(x > 4 for x in lista):
    print("Al menos un elemento de la lista es mayor que 4")
else:
    print("Ningún elemento de la lista es mayor que 4")

# filter(): Crea un iterador que devuelve los elementos de la secuencia que satisfacen una condición determinada.
# Por ejemplo:
lista = [1, 2, 3, 4, 5]
mayores_que_3 = filter(lambda x: x > 3, lista)
for x in mayores_que_3:
    print(x)

# map(): Crea un iterador que aplica una función a cada elemento de la secuencia. Por ejemplo:
python
Copy code
lista = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, lista)
for x in cuadrados:
    print(x)

# reduce(): Aplica una función acumulativa a todos los elementos de la secuencia y devuelve el resultado final. 
# Por ejemplo:
from functools import reduce
lista = [1, 2, 3, 4, 5]
def multiplicar(x, y):
    return x * y
producto = reduce(multiplicar, lista)
print(producto)
# En este ejemplo, la lista tiene cinco elementos: [1, 2, 3, 4, 5]. La función reduce() primero aplica 
# multiplicar(1, 2) a los dos primeros elementos de la lista (1 y 2), lo que devuelve 2. Luego, aplica 
# multiplicar(2, 3) lo que devuelve 6.Luego, aplica multiplicar(6, 4), hasta llegar al ultimo elemento