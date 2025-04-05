nombre = input("Ingrese su nombre: ")
seleccion = int(input("Seleccione la opción deseadad: \n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. "))

if seleccion == 1:
    print(nombre.upper())
elif seleccion == 2:
    print(nombre.lower())
elif seleccion == 3:
    print(nombre.title())
else:
    print("Selecionar una opción válida")