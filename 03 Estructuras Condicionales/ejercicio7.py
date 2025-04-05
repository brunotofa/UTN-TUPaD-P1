frase = input("Ingrese frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase = frase + "!"
    print(frase)
else:
    print(frase)