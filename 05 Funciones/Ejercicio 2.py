#Definir funciones
def saludar_usuario(nombre):
    return (f'Hola {nombre}!')


#Programa Principal
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))