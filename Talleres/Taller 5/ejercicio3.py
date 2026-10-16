import sys
import heapq

input = lambda: sys.stdin.readline().strip()

outputs = []

while True:
    N = int(input())

    if N == 0:
        break

    numeros = []

    for _ in range(N):
        numeros.append(int(input()))

    # Convertir la lista en un min-heap
    heapq.heapify(numeros)

    costo = 0

    while len(numeros) > 1:

        # Sacar los dos números más pequeños
        a = heapq.heappop(numeros)
        b = heapq.heappop(numeros)

        # Realizar la suma
        suma = a + b

        # El costo de esta operación es la suma
        costo += suma

        # El resultado vuelve a estar disponible
        heapq.heappush(numeros, suma)

    outputs.append(str(costo))

sys.stdout.write('\n'.join(outputs))