a = 10
b = 6
c = a * b
e = a * b
d = "AngelD"
e += 1 
print(c)
print(d)
print(e)

# Concatenar 
nombre = "lucas"
apellido = "perez"
edad= 34
name_completo = "su nombre es "+ nombre +" "+ apellido
name_edad = nombre + " " + apellido + f" y su edad es {edad}"   # el resultado es constinuo
name_edad2 = nombre," ", apellido," y su edad es:", edad        # el resultado es como un vector (la dif de usar comas(,) o el signo mas(+))
print(name_completo)
print(name_edad)
print(name_edad2)

# Operadores
# (del) elimina la variable
del edad 
# (in / not in) operador de pertenencia
print("lucas" in name_completo)
print("perez" not in name_completo)
