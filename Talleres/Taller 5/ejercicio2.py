import sys

input = lambda: sys.stdin.readline().strip()

outputs = []

while True:
    N = int(input())

    if N == 0:
        break

    eventos = []

    for _ in range(N):
        inicio, fin = map(int, input().split())

        eventos.append((inicio, 1))
        eventos.append((fin, -1))

    # En caso de empate, -1 se procesa antes que +1
    eventos.sort()

    personas = 0
    max_personas = 0

    for tiempo, cambio in eventos:
        personas += cambio
        max_personas = max(max_personas, personas)

    # María José es una de las personas
    amigos = max_personas - 1

    outputs.append(str(amigos))

sys.stdout.write('\n'.join(outputs))