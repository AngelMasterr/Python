# En "llamar_txt.py" se explica como llamar los archivos, revisar
# "w": da permisos para poder escrbir en el archivo, 
with open("Archivos//archivo_texto.txt", "w", encoding="UTF-8") as archivo:
    # write: Sobreescribe en el archivo y borra todo lo que tenia antes, TENGA CUIDADO
    archivo.write("Angel eres hermosos putito")  

with open("Archivos//archivo_texto.txt", "w", encoding="UTF-8") as archivo:
    # writelines: Sobreescribe en varias lineas, usando "\n" para bajar a la otra linea 
    archivo.writelines(["Angel eres hermosos putito \n", "Eres superinteligente baby"]) 