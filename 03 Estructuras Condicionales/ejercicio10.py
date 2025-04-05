hemisferio = input("En qué hemisferio se encuentra? (Ingrese N para Norte o S para Sur): ").strip().upper()
mes = int(input("Ahora ingrese mes del año (del 1 al 12): "))
dia = int(input("Ahora el día del año (del 1 al 31): "))

def variable_estacion(hemisferio, mes, dia):
    if hemisferio == "N" or "n":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            return "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            return "Verano"
        else:
            return "Otoño"
    elif hemisferio == "S"or "s":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            return "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            return "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            return "Invierno"
        else:
            return "Primavera"
    else:
        return "Hemisferio no válido"

if 1 <= mes <= 12 and 1 <= dia <= 31:
    estacion = variable_estacion(hemisferio, mes, dia)
    print(f'La estación del año en el hemisferio {hemisferio} es: {estacion}')
else:
    print("Ingrese mes y día válidos")

