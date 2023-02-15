
archvio = open("Archivos//archivo_texto.txt", encoding="UTF-8") 
# IMPORTANTE: No poner en la primera linea de codigo comentarios cuando se llaman archivos, puede salir error, con "with" si se puede
# open: Llamar un archvio que este dentro de la misma carpeta
# encoding: para que codificque el texto en un lenguaje universal "UTF-8" (se hace porque a veces no reconoce bien todos los caracteres)

leer_archvio = archvio.read()
leer_primera_linea = archvio.readline()
leer_todas_lineas = archvio.readlines()
archvio.close()

# Solo se ejecuta la primera variable "leer archivo", cuando se llama el archivo es necesario cerrarlo y volverlo abrir 
# para llamar otra variable, siempre debe usarse "close"
print(leer_primera_linea) # No muestra nada debdio a que el archivo lo esta usando "leer archivo" y no se ha cerrado


# with: Este bloque asegura que el archivo se cierre automáticamente después de que se hayan leído todos los datos
with open("Archivos//archivo_texto.txt", encoding="UTF-8") as archivo:
    
    leer_archvio = archivo.read()    
    print(leer_archvio) # No es ncesario cerrarlo 

with open("Archivos//archivo_texto.txt", encoding="UTF-8") as archivo:
    
    leer_primera_linea = archivo.readline()    
    print(leer_primera_linea) # No es ncesario cerrarlo 

with open("Archivos//archivo_texto.txt", encoding="UTF-8") as archivo:
    
    leer_todas_lineas = archivo.readlines()    
    print(leer_todas_lineas) # No es ncesario cerrarlo 