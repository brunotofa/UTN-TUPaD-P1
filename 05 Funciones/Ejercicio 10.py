#Definir funciones
def calcular_promedios(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2)

#Programa principal
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese el segundo: "))
num3 = int(input("Ahora el último: "))

promedio = calcular_promedios(num1, num2, num3)
print(f'El promedio obtenido es {promedio}')