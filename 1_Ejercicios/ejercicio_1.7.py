# repasando conceptos basicos en python - CICLOS


def verificar_si_puede_conducir(edad):
   if edad >= 18:
      print("Usted puede conducir perrito")
   else:
      print("NO puede conducir, eres menor de edad")

edades = [18, 15, 36, 25, 12]

for edad in edades:
   verificar_si_puede_conducir(edad)
