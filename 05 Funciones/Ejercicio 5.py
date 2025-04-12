#Definir funciones
def segundos_a_horas(segundos):
    return (segundos / 3600)

#Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
while segundos <= 0:
    segundos = int(input("Los segundos deben ser mayor a cero, intente otra vez: "))

print(f'{segundos} son {segundos_a_horas(segundos)} horas')