import sys
import heapq

input = lambda: sys.stdin.readline().strip()

C = int(input())
outputs = []

for _ in range(C):

    N = int(input())

    trabajos = []
    total_pataletas = 0

    for _ in range(N):
        hora, pataleta = map(int, input().split())

        deadline = hora // 10

        trabajos.append((deadline, pataleta))
        total_pataletas += pataleta

    # Procesar los deadlines de menor a mayor
    trabajos.sort()

    heap = []

    for deadline, pataleta in trabajos:

        # Intentamos guardar este niño como uno atendido a tiempo
        heapq.heappush(heap, pataleta)

        # Hasta este deadline existen deadline + 1 turnos
        if len(heap) > deadline + 1:
            # Sacamos la menor pataleta
            heapq.heappop(heap)

    # Las pataletas que evitamos
    evitadas = sum(heap)

    # Las restantes son las pataletas que tendrá
    respuesta = total_pataletas - evitadas

    outputs.append(str(respuesta))

sys.stdout.write('\n'.join(outputs))