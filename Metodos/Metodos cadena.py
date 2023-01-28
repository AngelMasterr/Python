cadena1 = "hello i am angel"
Cadena2 = "your welcome"
cadena3 = "YOU ARE WONDERFULL"
cadena4 = "1234567890"

# dir : funcion que muestra todos los metodos que puedo aplicar a un obejto (string, int, flota, etc)
# print(dir(cadena1)) 

# METODOS
# upper() : Convierte todo a mayuscula
print(cadena1.upper()) 

# lower() : Convierte todo a minuscula
print(cadena3.lower()) 

# capitalize : coniverte todo en minuscula y deja la primera letra en mayuscula
print(cadena3.capitalize())

# find() : busca la posicion de un dato en una cadena, si no la encunetra devuevle (-1)
print(cadena1.find("i"))
print(cadena1.find("am"))

# index() : busca la posicion de un dato en una cadena, si no la encunetra devuelve una excepcion (error)
print(cadena1.index("i"))
print(cadena1.index("am"))

# isnumeric() : si la cadena de texto solo son numeros devuelve (true) de lo contrario (false)
print(cadena4.isnumeric())

# count() : cuantas veces se encuentra un dato en una cadena
print(cadena1.count("a"))

# len : no es un metodo, es una funcion que cuenta todo los caracteres de  la cadena
print(len(cadena1))

# startswith() : verifica si la cadena empieza por el dato dado (true o false)
print(cadena1.startswith("hel"))

# endswith() : verifica si la cadena termina por el dato dado (true o false)
print(cadena1.endswith("gel"))

# replace() : reemplaza un pedazo de la cadena por el dato dado, si no encuentra coincidencia no hace nada
print(cadena1.replace("angel", "DarkAngel"))

# split() : separa la cadena en donde encuentre el dato dado y la convierte el lista
print(cadena1.split(" ")) # separa la cadena cada vez que encuentre "espacio"