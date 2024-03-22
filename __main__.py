from Package.LoginUser import LoginUser


def main():
    name = input("Enter your name: ")
    lastname = input("Enter your lastname: ")
    phone = input("Enter your phone: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = LoginUser(name, lastname, phone, email, password)
    print(user)


if __name__ == "__main__":
    main()

