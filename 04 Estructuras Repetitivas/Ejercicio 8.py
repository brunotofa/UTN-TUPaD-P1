# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. 


#Se declaran las variable que necesitamos
num_positivo = 0
num_negativo = 0
num_par = 0
num_impar = 0

#Se genera el bucle
for i in range(1, 101):
    numero = int(input("Ingresar un número: "))
    if numero > 0:
        num_positivo +=1
    else:
        num_negativo +=1
    if numero % 2 == 0:
        num_par +=1
    else:
        num_impar +=1

print("Cantidad de números positivos:", num_positivo)
print("Cantidad de números negativos:", num_negativo)
print("Cantidad de números pares:", num_par)
print("Cantidad de números impares:", num_impar)
