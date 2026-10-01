import sys

input = lambda: sys.stdin.readline().strip()

outputs = []

while True:
    N = int(input())

    if N == 0:
        break

    fortalezas = []

    for _ in range(N):
        S, K, B = map(int, input().split())

        perdidas = K + B
        necesarios = max(S, perdidas)

        # Cuántos soldados adicionales exige esta fortaleza
        prioridad = necesarios - perdidas

        fortalezas.append((prioridad, necesarios, perdidas))

    # Mayor prioridad primero
    fortalezas.sort(reverse=True)

    soldados_perdidos = 0
    respuesta = 0

    for prioridad, necesarios, perdidas in fortalezas:

        # Soldados iniciales necesarios para poder llegar a esta fortaleza
        respuesta = max(
            respuesta,
            soldados_perdidos + necesarios
        )

        soldados_perdidos += perdidas

    outputs.append(str(respuesta))

sys.stdout.write('\n'.join(outputs))