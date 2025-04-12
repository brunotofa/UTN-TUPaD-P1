#Definir funciones
def calcular_imc(peso, altura):
    if altura <= 0:
        return "Altura no valida"
    imc = peso / (altura ** 2)
    return imc



#Programa principal
peso = float(input("Ingrese el peso (en kg): "))
altura = float(input("Ahora la altura (en mts): "))

resultado = calcular_imc(peso, altura)
print(f'El IMC obtenido es {resultado:.2f}')