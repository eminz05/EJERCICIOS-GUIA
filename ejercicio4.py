usuarios = []
claves = []

while True:
    print("---Menú---")
    print("1. Inicio Sesión")
    print("2. Registrar Usuario")
    print("3. Eliminar Usuario")
    print("4. Salir")

    while True:
        try:
            opc = int(input("Ingrese su opción: "))
            if opc > 4 or opc < 1:
                print("Por favor seleccione una opción entre 1 y 4")
            else:
                break
        except ValueError:
            print("Ingrese nuevamente una opción válida")
    if opc == 4:
        print("Gracias por preferirnos...vuelve pronto")
        break
    elif opc == 1:
        user = input("Usuario: ")
        passw = input("Contraseña: ")
        if user in usuarios:
            pos = usuarios.index(user)
            if claves[pos] == passw:
                print("Inicio de sesión exitosa")
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no encontrado")
    elif opc == 2:
        user = input("Usuario: ")
        passw = input("Contraseña: ")
        usuarios.append(user)
        claves.append(passw)
        print("Usuario registrado correctamente!")
    elif opc == 3:
        user = input("Ingrese usuario a eliminar: ")
        if user in usuarios:
            pos = usuarios.index(user)
            passw = input("Ingrese la contraseña para confirmar: ")
            if claves[pos] == passw:
                claves.pop(pos)
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no encontrado!")
            




