# Cuando un modulo se ecnuentre dentro de una carpeta que esta dentro de esta carpeta "Modulos", es necesario 
# especificar la carpeta interna para llamarlo
import mas_modulos.modulo_saludar
print(mas_modulos.modulo_saludar.Saludar("angel"))


# sys: es un modulo construido en python
# path: nos muestra todas las rutas que puede utilizar en este archivo, de donde podemos importar las funciones,
#       metodos, variables, etc. 
import sys
print(sys.path)


# Si el modulo se encuentra en una carpeta diferente a la carpeta donde se encuentra este archivo "Modulos" 
# es necesario importar la ruta de la carpeta donde se encuentra el modulo a utilizar, en este caso vamos a usar el modulo 
# ejercicio_nivel_2.3 que se encuentra en la carpeta "2_Ejercicios"

sys.path.append("D:\\ANGEL\\Programacion\\Python\\2_Ejercicios")
print(sys.path) 
# Ahora ya nos muestra la ruta que acabamos de introducir para poder llamar el modulo que necesitamos
import ejercicio_nivel_23
print(ejercicio_nivel_23)


# El modulo "ejercicio_nivel_23" contiene varias funciones y solo necesito llamar la función "metodo_crivo"
from ejercicio_nivel_23 import metodo_crivo
print(metodo_crivo(15))

