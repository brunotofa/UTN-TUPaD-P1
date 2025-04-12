#Definir funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", (i*numero))

#Programa principal
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)