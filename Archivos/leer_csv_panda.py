# pandas: es mas practico que "csv" y el diminutivo mas usado es "pd" 

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

# Si queremos asignar el nombre de la columnas lo podemos hacer desde la lectura
dataframe = pd.read_csv("Archivos//1archivo_csv.csv", names=["name","age","gender"])
print(dataframe)