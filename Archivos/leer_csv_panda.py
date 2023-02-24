# pandas: es mas practico que "open" y el diminutivo mas usado es "pd" 

# se debe instalar "pip" desde el terminal de window "cmd - adminstrador" (py -m ensurepip --upgrade)
# para verficar si quedo instalado y todo lo que tiene (py -m pip) 
# luego instalar pandas (py -m pip install pandas)

import pandas as pd

dataframe = pd.read_csv("Archivos//1archivo_csv.csv")
print(dataframe)

# Obtener datos de una sola columna
nombre = dataframe["Nombre"]
edad = dataframe["Edad"]
genero = dataframe["Genero"]
print(genero)

# names: Si queremos agregar el nombre de las columnas lo podemos hacer desde la lectura
dataframe = pd.read_csv("Archivos//1archivo_csv.csv", names=["name","age","gender"])
print(dataframe)

# sort_values: para ordenar los valores de manera ascendente
dataframe = pd.read_csv("Archivos//1archivo_csv.csv")
ordenar_edad_ascend = dataframe.sort_values("Edad")
print(ordenar_edad_ascend)

# sort_values: para ordenar los valores de manera descendente
ordenar_edad_descen = dataframe.sort_values("Edad", ascending=(False))
print(ordenar_edad_descen)