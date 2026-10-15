import sys
import heapq

def dijkstra(grafo, origen=0):
    n = len(grafo)
    INF = float("inf")

    distancias = [INF] * n
    distancias[origen] = 0

    heap = [(0, origen)]

    while heap:
        distancia_actual, u = heapq.heappop(heap)

        # Ignorar entradas desactualizadas del montículo
        if distancia_actual != distancias[u]:
            continue

        for v, dificultad in grafo[u]:
            nueva_distancia = distancia_actual + dificultad

            if nueva_distancia < distancias[v]:
                distancias[v] = nueva_distancia
                heapq.heappush(heap, (nueva_distancia, v))

    return distancias


def resolver():
    datos = list(map(int, sys.stdin.buffer.read().split()))

    if not datos:
        return

    pos = 0
    N = datos[pos]
    M = datos[pos + 1]
    pos += 2

    P = datos[pos]
    pos += 1

    # Los escondites están identificados desde 0 hasta N
    grafo = [[] for _ in range(N + 1)]

    for _ in range(M):
        u = datos[pos]
        v = datos[pos + 1]
        dificultad = datos[pos + 2]
        pos += 3

        grafo[u].append((v, dificultad))
        grafo[v].append((u, dificultad))

    # Calcular todas las distancias desde el origen una sola vez
    distancias = dijkstra(grafo)

    salida = []

    for _ in range(P):
        destino = datos[pos]
        pos += 1

        if distancias[destino] == float("inf"):
            salida.append("ZOMBI")
        else:
            salida.append(str(distancias[destino]))

    sys.stdout.write("\n".join(salida))

resolver()
