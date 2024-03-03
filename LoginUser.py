print("Bienvenido al ingreso de sus datos. No piense que usaremos esto para estafarlo 🥹")


class LoginUser:
    def __init__(self, name, lastname, phone, email, password):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.password = password
        self.dataUser = []

    def adddatainfo(self):
        self.name = input("Ingrese su nombre: ")
        self.dataUser.append(self.name)
        self.lastname = input("Ingrese su apellido: ")
        self.dataUser.append(self.lastname)
        self.phone = input("Ingrese su número de teléfono: ")
        self.dataUser.append(self.phone)
        self.email = input("Ingrese su correo electrónico: ")
        self.dataUser.append(self.email)
        self.createsecurepassword()
        return self.dataUser

    def createsecurepassword(self):
        self.password = input("Por favor cree una contraseña: ")
        if len(self.password) < 8 or len(self.password) > 16 or not self.password.isalnum() or self.password.isalpha() or self.password.isdigit():
            print("La contraseña debe tener al menos 8 caracteres y contener tanto letras como números.")
            self.password = input("Por favor cree una contraseña: ")
        else:
            print("Contraseña creada correctamente.")
            self.dataUser.append(self.password)

        return self.dataUser


export = LoginUser
