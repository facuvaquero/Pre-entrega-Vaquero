base_de_datos = {}

def registrar_usuario():
    nombre_usuario = input("Ingrese su nombre de usario: ")
    if nombre_usuario in base_de_datos:
        print("El usuario ya esta registrado")
        return
    contraseña = input("Ingrese su contraseña: ")
    base_de_datos[nombre_usuario] = contraseña
    print("Registro exitoso")

def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if nombre_usuario in base_de_datos:
        if base_de_datos[nombre_usuario] == contraseña:
            print("Inicio de sesion exitoso!")   
        else:
            print("Contraseña incorrecta")
    else:
        print("Nombre de usuario no registrado.")        

def menu():
    while True:
        print("Menu:")
        print("1 - Registrase: ")
        print("2 - Iniciar sesion: ")
        print("3 - Salir")
        opcion = input("Seleccione una opcion 1,2,3:")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()    
        elif opcion == "3":
            print("Fin del programa.")
        else:
            print("Opcion no valida, intente de nuevo.")
                 
menu()