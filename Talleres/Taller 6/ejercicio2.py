import sys
import math

def prim(puntos):
    n = len(puntos)

    # Distancia mínima conocida desde el árbol hasta cada punto
    distancias = [float("inf")] * n
    visitados = [False] * n

    distancias[0] = 0.0
    total = 0.0

    for _ in range(n):
        # Elegir el punto no visitado más cercano al árbol.
        u = -1
        for i in range(n):
            if not visitados[i] and (
                u == -1 or distancias[i] < distancias[u]
            ):
                u = i

        visitados[u] = True
        total += distancias[u]

        x1, y1 = puntos[u]

        # Actualizar las distancias hacia los puntos restantes
        for v in range(n):
            if not visitados[v]:
                x2, y2 = puntos[v]
                distancia = math.hypot(x1 - x2, y1 - y2)

                if distancia < distancias[v]:
                    distancias[v] = distancia

    return total


def resolver():
    datos = sys.stdin.buffer.read().split()
    if not datos:
        return

    pos = 0
    T = int(datos[pos])
    pos += 1

    salida = []

    for _ in range(T):
        N = int(datos[pos])
        pos += 1

        puntos = []

        for _ in range(N):
            x = float(datos[pos])
            y = float(datos[pos + 1])
            pos += 2
            puntos.append((x, y))

        longitud = prim(puntos)
        salida.append(f"{longitud:.1f}")

    sys.stdout.write("\n".join(salida))

resolver()
