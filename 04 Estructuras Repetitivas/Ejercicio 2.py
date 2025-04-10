#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 


print("Ingrese un número entero: ")
numero = int(input())

#Con el comando len() verificamos la cantidad de caracteres que tiene un string
#Por eso se convierte primero el número a string con el comando str() y luego se aplica len()
print("El número", numero, "tiene", len(str(numero)), "dígitos")