print("Bienvenido al ingreso de sus datos. No piense que usaremos esto para estafarlo 🥹")
class Database:
    def __init__(self):
        self.base = []

    def addInfo(self):
        name = input("Ingrese su nombre: ")
        lastname = input("Ingrese su apellido: ")
        age = input("Ingrese su edad: ")
        email = input("Ingrese su correo: ")
        self.base.append({'name': name, 'lastname': lastname, 'age': age, 'email': email})
        input("Datos ingresados correctamente. Presione enter para continuar")
        print("Gracias por confiar en nosotros. No le robaremos su dinero 🤑")

    def showBase(self):
        for info in self.base:
            print(info)

db = Database()
db.addInfo()
db.showBase()

