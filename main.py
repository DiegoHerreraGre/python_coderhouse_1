from Package import LoginUser as lu

print("Bienvenido al ingreso de sus datos. No piense que usaremos esto para estafarlo 🥹")

user = lu.LoginUser(name=None, lastname=None, password="password", email="email", phone=None)

user.adddatainfo()
def mainlogin ():
    input_user = input('Ingrese su usuario: ')

    if input_user == user.email:
        pass
    else:
        print('Usuario incorrecto')
        return mainlogin()

    input_password = input('Ingrese su contraseña: ')

    if input_password == user.password:
        pass
    else:
        print('Contraseña incorrecta')
        return mainlogin()

    print('Bienvenido al sistema')

mainlogin()