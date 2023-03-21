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
        print("{} esta ladrando".format(self.nombre))
        
    def comer(self):
        print("{} esta comiendo".format(self.nombre))
    
    def jugar(self):
        print("{} esta jugando".format(self.nombre))
        
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print("El perro ahora se llama {}".format(nombre))
        
# Instanciar un obejto
my_dog = Perro("Bobis", "chand", "marron")
# llamara un metodo o atributo de la clase "Perro" la cual esta en "my_dog"
my_dog.comer()
my_dog.ladrar()
my_dog.jugar()
my_dog.edad = "5 años"
print(my_dog.nombre,"tiene", my_dog.edad)
my_dog.cambiar_nombre("Alucard")
