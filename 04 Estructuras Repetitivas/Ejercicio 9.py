# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores.


#Delaramos las variables
cont = 0
suma = 0

#Entramos al bucle
for i in range(1, 101):
    numero = int(input("Ingresar un número: "))
    cont +=1
    suma += numero

print("La media de los números ingresados es:", (suma / cont))