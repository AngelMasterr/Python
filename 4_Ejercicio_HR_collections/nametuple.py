# namedtuple es una función integrada en Python que se utiliza para crear tuplas con campos de nombres 
# predefinidos. La tupla creada con namedtuple es similar a una clase, en el sentido de que cada campo 
# tiene un nombre y se puede acceder a él utilizando el nombre del campo.

# Calcular el promedio de calificación de los estudiantes (sum(MARKS)/studiants)
# la primera entrada contiene la cantidad de estudiantes n, la segunda el nombre de las variables de la tupla (ID, NAME, MARKS, CLASS)
# la sigueinte entrada los valores de cada estduainte

"""imput()
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   """

from collections import namedtuple

students = int(input())
name_colum = namedtuple("name_colum", (input().split()))
prom = 0
for i in range(students):
    date = name_colum(*input().split())    
    prom += int(date.MARKS)
print(prom/students)