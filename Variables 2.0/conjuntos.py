# set : creando un conjunto con set
conjunto = set(["dato1", "dato2"])
print(conjunto)
print(type(conjunto))

# creando un conjunto con solo llaves
conjunto = {"dato1", "dato2"}
print(conjunto)
print(type(conjunto))

# teoría de conjuntos (conjuntos, subconjuntos, superconjuntos)
conjunto_1 = {1, 3, 5, 7, 9}    #Conjutno A         - Superconjunto de B
conjunto_2 = {1, 3, 9}          #Subconjunto de A   - Conjunto B    

# Subconjunto: que tiene una parte de los datos del conjunto a analizar
# Superconjutno: que tiene los datos y mas del conjunto a analizar

resultado_1 = conjunto_2.issubset(conjunto_1) # issubset: verifica si conjunto_2 es un subconjunto de conjunto_1
resultado_1 = conjunto_2 <= conjunto_1 # verifica que todos los datos del conjunto 2 esten en el 1, lo mismo que issubset
print(resultado_1) 

resultado_2 = conjunto_1.issuperset(conjunto_2) # issuperset: verifica si conjunto_1 es un superconjunto de conjunto_2
resultado_2 = conjunto_1 > conjunto_2 # verifica que algunos datos del conjunto 1 esten en el 2, lo mismo que issuperset
print(resultado_2) 

# Verificar que no haya ningun numero en comun entre los conjuntos a analizar
resultado_3 = conjunto_2.isdisjoint(conjunto_1)
print(resultado_3)
