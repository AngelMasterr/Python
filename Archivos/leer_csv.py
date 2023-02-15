# csv: valores separados por comas, cada fila representa un registro y cada columna representa un campo dentro de ese registro
import csv
with open("Archivos//1archivo_csv.csv") as archivo_csv:
    reader = csv.reader(archivo_csv) #csv.reader: lee el archivo y toma cada fila como una tupla de valores que estan separados por comas
    for row in reader:
        print(row)