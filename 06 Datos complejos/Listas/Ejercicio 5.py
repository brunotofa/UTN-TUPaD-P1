#  Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza:

numeros = [8, 15, 3, 22, 7]        #Se crea la lista con los elementos
numeros.remove(max(numeros))       #Se indica con el método remove() que se elimine un elemento de la lista, con el método max() se indica
print(numeros)                     # que el elemento sea el mayor de la lista, se espera que se imprima [8, 15, 3, 7]