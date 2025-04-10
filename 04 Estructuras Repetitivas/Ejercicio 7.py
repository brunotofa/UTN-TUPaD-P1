# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.


suma = 0
numero = int(input("Ingrese un número positivo: "))

if numero <= 0:
    print("El número debe ser mayor a cero")
else:
    for i in range(0, numero+1): #Entramos al bucle donde se van a sumar los números
        suma += i
    print("La suma de los números entre 0 y", numero,"es:", suma)