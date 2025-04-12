#Definir funciones
def celcius_a_fahrenheit(numero):
    fahrenheit = (numero * 1.8) + 32
    return fahrenheit


#Programa principal
celcius = float(input("Ingrese la temperatura (°C): "))
print(f'{celcius} °C equivalen a {celcius_a_fahrenheit(celcius)}°F')
