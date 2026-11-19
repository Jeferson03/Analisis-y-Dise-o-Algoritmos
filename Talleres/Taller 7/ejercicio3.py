
import sys

def resolver():
    datos = iter(sys.stdin.buffer.read().split())
    salida = []

    INF = float("inf")

    while True:
        try:
            N = int(next(datos))
        except StopIteration:
            break
        
        if N == 0:
            break

        # Construir la matriz de distancias
        dist = []

        for i in range(N):
            fila = []

            for j in range(N):
                valor = next(datos)

                if valor == b'-':
                    fila.append(INF)
                else:
                    fila.append(int(valor))

            dist.append(fila)

        # Floyd-Warshall
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Buscar la mayor distancia mínima entre ciudades conectadas
        respuesta = 0

        for i in range(N):
            for j in range(i + 1, N):
                if dist[i][j] != INF:
                    respuesta = max(respuesta, dist[i][j])

        salida.append(str(respuesta))

    sys.stdout.write("\n".join(salida))



resolver()
