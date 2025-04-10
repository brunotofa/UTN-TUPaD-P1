#  Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#  secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#  un 0. 


suma = 0 #Se declara la variable que va a contenes la suma de los números ingresados

numero = int(input("Ingrese un número (cero para terminar): ")) #Se pide el primer número al usuario

while numero != 0:
    suma += numero #En esta instrucción se van sumando los números
    numero = int(input("Ingrese un número (cero para terminar): "))

print("La suma total es: ",suma)
