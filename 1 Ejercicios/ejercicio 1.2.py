# Suponiendo que una persona promedio habla dos palabras por segundo, pedirle al usuario que introduzco un texto,
# calcular cuanto tardaria en decir esa frase y cuantas palabras dijo
# si tarda mas de 10 segundos decirle "para mi hermano, no te pedi un testamento"
# Si hablo un 30% mas rapido, cunato tardaria yo en decir la frase

texto = input("Introduzca el texto de su agrado: ")
print("te voy a calcular cuanto tardaría en decirlo")

texto_separado = texto.split(" ")
cant_palabras = len(texto_separado)
if(cant_palabras/2 > 10):
    print(f"dijiste {cant_palabras} palabras en el texto dado, por lo tanto te tardaste {cant_palabras/2} segundos en decirlo")
    print("pará mi hermano, no te pedi un testamento")
else:
    print(f"dijiste {cant_palabras} palabras en el texto dado, por lo tanto te tardaste {cant_palabras/2} segundos en decirlo")

# si hablo un 30% mas rapido cuanto tardaría?
print(f"y yo que soy el mas rapido tarde {cant_palabras/2 * 0.7} segundos mi pez")