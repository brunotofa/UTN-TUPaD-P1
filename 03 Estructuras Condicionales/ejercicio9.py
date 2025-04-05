magnitud = float(input("Ingrese la magnitud del terremoto: "))

MUY_LEVE =3
LEVE = 4
MODERADO = 5
FUERTE = 6
MUY_FUERTE =7

if magnitud < MUY_LEVE:
    print("Según la escala de Richter se considera al terremoto muy leve")
elif magnitud < LEVE:
    print("Según la escala de Richter se considera al terremoto leve")
elif magnitud < MODERADO:
    print("Según la escala de Richter se considera al terremoto moderado")
elif magnitud < FUERTE:
    print("Según la escala de Richter se considera al terremoto fuerte")
elif magnitud < MUY_FUERTE:
    print("Según la escala de Richter se considera al terremoto muy fuerte")
elif magnitud >= MUY_FUERTE:
    print("Según la escala de Richter se considera al terremoto extemo")
else:
    print("Ingrese un número correcto")