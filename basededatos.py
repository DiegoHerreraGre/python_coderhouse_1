print("Bienvenido al ingreso de sus datos. No piense que usaremos esto para estafarlo 🥹")
class Database:
    def __init__(self):
        self.base = []

    def addInfo(self):

        name = input("Ingrese su nombre: ")
        lastname = input("Ingrese su apellido: ")

        ageIsValid = False
        while not ageIsValid:
            age = input("Ingrese su edad: ")
            if age.isdigit():
                age = int(age)
                if age >= 0:
                    ageIsValid = True
                else:
                    print("Edad inválida. Por favor, ingrese un número entero positivo")
            else:
                print("Edad inválida. Por favor, ingrese un número entero")

        emailValidator = False
        while not emailValidator:
            email = input("Ingrese su correo: ")
            if "@" in email and "." in email:
                emailValidator = True
            else:
                print("Correo inválido. Por favor, ingrese un correo válido 🤬🤬🤬")

        self.base.append({'name': name, 'lastname': lastname, 'age': age, 'email': email})

        input("Datos ingresados correctamente. Presione enter para continuar")
        print("Gracias por confiar en nosotros. No le robaremos su dinero 🤑")

    def showBase(self):
        for info in self.base:
            print(info)

    def convertToDictionary(self):
        base_dict = {i: info for i, info in enumerate(self.base)}
        return base_dict

db = Database()
db.addInfo()
db.showBase()
base_dict = db.convertToDictionary()
print(base_dict)