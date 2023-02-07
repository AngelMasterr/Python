# Import: importa el modulo deseado
import modulo_saludar

# La funcion "saludar" que esta dentro del medulo "modulo_saludar" ahora se convierte en un metodo
saludo = modulo_saludar.Saludar("angel")
print(saludo)

# as: es una forma de cambiar el nombre de un modulo o si importamos una funcion del modulo
import modulo_saludar as mod_saludar
saludo = mod_saludar.Saludar("eduardo")
print(saludo)

# from: cuando tenemos muchas funciones en un modulo y solo queremos llamar las que necesitamos (tambien puede importar variables)
# esto nos ayuda a trabajar con esa función sin necesidad de llamar a todo el modulo completo
from modulo_saludar import Saludar
saludo = Saludar("angeluz")  
print(saludo)

# ahora vamos a importar dos funcion del "modulo_saludar"
from modulo_saludar import Saludar, Despedirse
saludo = Saludar("angelmasterr")
despedida = Despedirse("angelmasterr")
print(saludo) 
print(despedida)

# dir: para ver las propiedades y metodos de la funcion
print(dir(modulo_saludar))