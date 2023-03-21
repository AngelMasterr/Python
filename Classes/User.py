class User_regular:
    def __init__(self):
        self.email = input("Introduzca su email: ")
        # __: para que el atributo sea privado y no se pueda llamar
        self.__pasword = input("Introduzca su contraseña: ")
        self.permissions = ["edit", "create", "update"]
        
    def setear_username(self):
        self.username = input("Introduzca su username: ")
        print("Username cambiado a: {}".format(self.username))
        
class User_pro(User_regular): # hereda los metodos de "User_regular"
    def __init__(self):
        super().__init__() # hereda los atributos de "User_regular"
        self.permissions += ["delete", "download"] # se aregan mas cositas
        
    def pay_suscription(self, monto):
        self.monto = monto
        print("Usted ha pagado exitosamente su suscripcion ({})".format(self.monto))
        
class User_manager:
    def create_user(self, suscripcion):
        if suscripcion: # si suscripcion es True ejecute el if
            user = User_pro()
        else:
            user = User_regular()
        print("Se ha creado exitosamente su usuario. Sus permisos son: {}".format(user.permissions))
        
User_manager().create_user(True) 
        
    