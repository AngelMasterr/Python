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