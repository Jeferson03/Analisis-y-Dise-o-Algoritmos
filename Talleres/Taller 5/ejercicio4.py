import sys

input = lambda: sys.stdin.readline().strip()

outputs = []

while True:
    N = int(input())

    if N == 0:
        break

    barcos = []

    for _ in range(N):
        L, R = map(int, input().split())
        barcos.append((L, R))

    # Ordenamos por el extremo derecho
    barcos.sort(key=lambda x: x[1])

    disparos = 0
    ultimo_disparo = -1

    for L, R in barcos:

        # Si el último disparo no está dentro del barco,
        # necesitamos realizar otro.
        if ultimo_disparo < L:
            disparos += 1
            ultimo_disparo = R

    outputs.append(str(disparos))

sys.stdout.write('\n'.join(outputs))