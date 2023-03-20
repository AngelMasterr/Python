class Perro:
    # constructor
    def __init__(self, nombre, raza, color):        
        self.color = color
        self.raza = raza
        self.nombre = nombre
        self.tamaño = None
        self.edad = None
        
    # metodos
    def ladrar(self):
        print("El perro esta ladrando")
        
    def comer(self):
        print("El perro esta comiendo")
    
    def jugar(self):
        print("El perro esta jugando")
        
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print("El perro ahora se llama {}".format(nombre))
        
# Instanciar un obejto
my_dog = Perro("Bobis", "chand", "marron")
# llamara un metodo o atributo de la clase "Perro" la cual esta en "my_dog"
my_dog.comer()
my_dog.edad = "5 años"
print(my_dog.nombre, my_dog.edad)
my_dog.cambiar_nombre("Alucard")
