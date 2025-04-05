edad = int(input("Ingrese su edad: "))

EDAD_MINIMA = 1
EDAD_NINIO = 12
EDAD_ADOLESCENTE = 18
EDAD_JOVEN = 30

if edad < EDAD_MINIMA:
    print("Ingrese edad correcta")
elif edad < EDAD_NINIO:
    print("Pertenece al grupo niños")
elif edad < EDAD_ADOLESCENTE:
    print("Pertenece al grupo adolescente")
elif edad < EDAD_JOVEN:
    print("Pertenece al grupo adulto joven")
else:
    print("Pertenece al grupo adulto")
