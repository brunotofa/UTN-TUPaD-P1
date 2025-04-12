#Definir funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        print("No se puede dividir por cero, intente otra vez!")
    return (suma, resta, multiplicacion, division)

#Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ahora el segundo: "))

resultados = operaciones_basicas(num1, num2)
print(f'La suma entre {num1} y {num2} es: {resultados[0]}')
print(f'La resta entre {num1} y {num2} es: {resultados[1]}')
print(f'La multiplicación entre {num1} y {num2} es: {resultados[2]}')
print(f'La división entre {num1} y {num2} es: {resultados[3]}')