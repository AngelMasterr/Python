# En "llamar_txt.py" se explica como llamar los archivos, revisar
# "a": append - da permisos para agregar texto al archvio, NO SOBREESCRIBE OSEA NO BORRA, 
with open("Archivos//1archivo_texto.txt", "a", encoding="UTF-8") as archivo:
    # agregando contenido al archivo existente con "writelines" para poder agregar mas de una linea
    archivo.writelines(["\n","Angel eres hermosos putito"])  
          
          
    # Escribir varias lineas de texto utilizando "write"    
    for i in range(1, 6):
        archivo.write("\n")
        archivo.write(f"{i} linea de texto")
        
    
    # Escribir varias lineas de texto utilizando "write" en una linea de codigo
    # ";" punto y coma sirve para separar cada accion
    for num in range(1, 6): archivo.write("\n"); archivo.write(f"{num} linea de texto mejorada")