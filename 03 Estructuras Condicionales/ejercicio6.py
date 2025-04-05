from statistics import mode, median, mean

import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f' moda:  {moda}')
print(f' mediana: {mediana}')
print(f' media: {media}')

if media > mediana and mediana > moda:
    print("Sesgo positivio o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No existe sesgo")