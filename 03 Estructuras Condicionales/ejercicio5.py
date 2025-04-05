contrasenia = input("Ingrese su contraseña (debe contener al menos 8 caracteres pero no más de 14): ")
caracteres_min = 8
caracteres_max = 14

if len(contrasenia) >= caracteres_min and len(contrasenia) <= caracteres_max:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña ente 8 y 14 carácteres")