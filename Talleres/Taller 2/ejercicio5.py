import sys

input = lambda: sys.stdin.readline().rstrip()

MAX = 100000

# divisores[x] = cantidad de divisores de x
divisores = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        divisores[j] += 1


# Marcar los números que pertenecen a la secuencia
nu_nu_do_n = [0] * (MAX + 1)

x = 1

while x <= MAX:
    nu_nu_do_n[x] = 1
    x += divisores[x]


# Prefix sum:
# prefijo[x] = cantidad de términos de la secuencia <= x
prefijo = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    prefijo[i] = prefijo[i - 1] + nu_nu_do_n[i]


N = int(input())

respuestas = []

for _ in range(N):
    A, B = map(int, input().split())

    cantidad = prefijo[B] - prefijo[A - 1]

    respuestas.append(str(cantidad))

sys.stdout.write("\n".join(respuestas))

