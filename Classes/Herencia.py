class Animal:
    def __init__(self):
        self.edad = None
        self.especie = None
        self.pelaje = None
    
    def comer(self):
        print("el animal esta comiendo")
        
    def reproducirse(self):
        print("el animal se esta reproduciendo")
    
# Heredar solo los metodos de la clase "Animal"
class Perro(Animal):
    def __init__(self, nombre):       
        # super().__init__(): nos permite tambien heredar los atributos de la clase "Animal"
        super().__init__()         
        # atributos propios de esta clase "Perro"
        self.raza = None
        self.nombre = nombre
        self.tamaño = None
    
    # metodos propios de esta clase "Perro"
    def ladrar(self):
        print("{} esta ladrando".format(self.nombre))  
    
    def jugar(self):
        print("{} esta jugando".format(self.nombre))


my_dog = Perro("bobis")
my_dog.jugar()
my_dog.reproducirse()
print(my_dog.edad) # imprimir un atributo de la clase "Animal"