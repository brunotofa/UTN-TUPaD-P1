#Definir funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return (f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ahora su apellido: ")
edad = input("Cuántos años tiene?: ")
residencia = input("Dónde vive?: ")

print(informacion_personal(nombre, apellido, edad, residencia))