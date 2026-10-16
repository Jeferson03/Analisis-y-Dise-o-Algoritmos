import sys
from collections import deque

def max_flow(n, conexiones):
    grafo = [[] for _ in range(n)]

    def agregar_arista(u, v, capacidad):
        # [destino, capacidad residual, índice de la arista inversa]
        arista_uv = [v, capacidad, len(grafo[v])]
        arista_vu = [u, 0, len(grafo[u])]

        grafo[u].append(arista_uv)
        grafo[v].append(arista_vu)

    for u, v, capacidad in conexiones:
        agregar_arista(u, v, capacidad)

    origen = 0
    destino = n - 1
    flujo_total = 0

    while True:
        # BFS: construir los niveles de la red residual
        nivel = [-1] * n
        nivel[origen] = 0
        cola = deque([origen])

        while cola:
            u = cola.popleft()

            for v, capacidad, _ in grafo[u]:
                if capacidad > 0 and nivel[v] == -1:
                    nivel[v] = nivel[u] + 1
                    cola.append(v)

        if nivel[destino] == -1:
            break

        # Posición de la siguiente arista por explorar en cada nodo
        actual = [0] * n

        def dfs(u, flujo):
            if u == destino:
                return flujo

            while actual[u] < len(grafo[u]):
                arista = grafo[u][actual[u]]
                v, capacidad, rev = arista

                if capacidad > 0 and nivel[v] == nivel[u] + 1:
                    enviado = dfs(v, min(flujo, capacidad))

                    if enviado > 0:
                        arista[1] -= enviado
                        grafo[v][rev][1] += enviado
                        return enviado

                actual[u] += 1

            return 0

        # Enviar todo el flujo posible en esta red de niveles
        while True:
            enviado = dfs(origen, float("inf"))

            if enviado == 0:
                break

            flujo_total += enviado

    return flujo_total


def resolver():
    datos = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0

    C = datos[pos]
    pos += 1

    salida = []

    for _ in range(C):
        N = datos[pos]
        M = datos[pos + 1]
        pos += 2

        conexiones = []

        for _ in range(M):
            u, v, capacidad = datos[pos:pos + 3]
            pos += 3
            conexiones.append((u, v, capacidad))

        salida.append(str(max_flow(N, conexiones)))

    sys.stdout.write("\n".join(salida))


resolver()
