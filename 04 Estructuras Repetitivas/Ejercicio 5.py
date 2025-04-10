# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random #Importamos la biblioteca

numero_random = random.randint(0, 9) #Generamos el número automáticamente
intentos = 1

numero = int(input("Adivine el número entre 0 y 9: "))
while numero != numero_random:
    intentos += 1
    print("Número incorrecto!")
    numero = int(input("Intente otra vez: "))

print("Muy bien! Adivinó, el número era:", numero_random)
print("Cantidad de intentos:", intentos)





