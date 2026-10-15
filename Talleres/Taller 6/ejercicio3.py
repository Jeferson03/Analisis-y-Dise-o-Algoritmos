import sys
import heapq

def dijkstra(matriz, n, m):
    INF = float("inf")

    distancias = [[INF] * m for _ in range(n)]
    distancias[0][0] = 0

    heap = [(0, 0, 0)]
    movimientos = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while heap:
        costo, fila, columna = heapq.heappop(heap)

        if costo != distancias[fila][columna]:
            continue

        if fila == n - 1 and columna == m - 1:
            return costo

        for df, dc in movimientos:
            nf = fila + df
            nc = columna + dc

            if 0 <= nf < n and 0 <= nc < m:
                nuevo_costo = costo + matriz[nf][nc]

                if nuevo_costo < distancias[nf][nc]:
                    distancias[nf][nc] = nuevo_costo
                    heapq.heappush(heap, (nuevo_costo, nf, nc))

    return distancias[n - 1][m - 1]


def resolver():
    datos = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0

    T = datos[pos]
    pos += 1

    salida = []

    for _ in range(T):
        n = datos[pos]
        m = datos[pos + 1]
        pos += 2

        matriz = []

        for _ in range(n):
            matriz.append(datos[pos:pos + m])
            pos += m

        salida.append(str(dijkstra(matriz, n, m)))

    sys.stdout.write("\n".join(salida))


resolver()

