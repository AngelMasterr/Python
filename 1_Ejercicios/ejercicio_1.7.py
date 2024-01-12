# repasando conceptos basicos en python - CICLOS

# MOstrar mensaje si tiene permiso para conducir
def verificar_si_puede_conducir(edad):
   if edad >= 18:
      print("Usted puede conducir perrito")
   else:
      print("NO puede conducir, eres menor de edad")

edades = [18, 15, 36, 25, 12]

for edad in edades:
   verificar_si_puede_conducir(edad)

# la misma funcion de arriba pero optiomizada
def verificar_si_puede_conducir_2(edades):
   for edad in edades:
      if edad >= 18:
         print("Usted puede conducir perrito")
      else:
         print("NO puede conducir, eres menor de edad")
      
verificar_si_puede_conducir_2(edades)


# Crear lista con valores tipo booleanos
verificar = []
edades = [18, 15, 20, 25, 12]
def verificar_si_puede_conducir_bool(edades):
   for edad in edades:
      if edad >= 18:
         verificar.append(True)
      else:
         verificar.append(False)         
   
   print(verificar)
verificar_si_puede_conducir_bool(edades)


mi_lista = [3, 2, 5, 4, 7, 3, 9]
valor_a_buscar = 3
# Utilizando filter
resultado_filter = list(filter(lambda x: x == valor_a_buscar, mi_lista))
print(resultado_filter)
if resultado_filter:
    print(f"¡Encontré el valor {valor_a_buscar} en la lista!")
else:
   print('No se encontro el resultado')