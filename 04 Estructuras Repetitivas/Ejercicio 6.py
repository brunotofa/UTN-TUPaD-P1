#  Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#  entre 0 y 100, en orden decreciente. 

for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)