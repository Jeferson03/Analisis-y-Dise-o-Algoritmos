import math
import sys


MAX_N = 100000

# Criba de Eratóstenes
primo = [True] * (MAX_N + 1)

primo[0] = primo[1] = False

for i in range(2, int(math.sqrt(MAX_N)) + 1):
    if primo[i]:
        for j in range(i * i, MAX_N + 1, i):
            primo[j] = False


# cantidad[i] = cantidad de primos <= i
cantidad = [0] * (MAX_N + 1)

for i in range(1, MAX_N + 1):
    cantidad[i] = cantidad[i - 1]

    if primo[i]:
        cantidad[i] += 1


# Leer entrada
datos = sys.stdin.read().split()

C = int(datos[0])

for i in range(1, C + 1):
    n = int(datos[i])

    P = cantidad[n]
    aproximacion = n / math.log(n)

    error = P - aproximacion

    print(round(error))