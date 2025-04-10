# Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ahora el segundo: "))

suma = 0

#Generamos un bucle
for i in range((numero1 + 1), numero2):
    suma += i

print("La suma de los números entre", numero1, "y",numero2, "es: ", suma)