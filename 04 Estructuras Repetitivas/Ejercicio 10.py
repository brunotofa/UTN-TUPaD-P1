# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingresar número: ")

if numero.startswith('-'):
    num_invertido = '-' + numero[:0:-1]
else:
    num_invertido = numero[::-1]

print("Número invertido:", num_invertido)
