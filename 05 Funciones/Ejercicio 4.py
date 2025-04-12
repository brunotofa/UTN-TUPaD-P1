from math import pi

#Definir funciones
def calcular_area_circulo(radio):
    return (pi * (radio * radio))

def calcular_perimetro_circulo(radio):
    return (2 * pi * radio)

#Programa principal
radio = float(input("Ingrese el radio del círculo: "))
print(f'El area del circulo es {calcular_area_circulo(radio)} y el perímetro es {calcular_perimetro_circulo(radio)}')