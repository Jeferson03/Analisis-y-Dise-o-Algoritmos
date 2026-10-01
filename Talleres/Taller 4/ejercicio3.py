import sys

input = lambda: sys.stdin.readline().strip()

C = int(input())
outputs = []

for _ in range(C):
    N = int(input())

    tapas = []

    for _ in range(N):
        tapas.append(int(input()))

    tapas.sort()

    izquierda = 0
    derecha = N - 1
    bebidas = 0

    while izquierda < derecha:

        if tapas[izquierda] + tapas[derecha] >= 1000:
            bebidas += 1
            izquierda += 1
            derecha -= 1

        else:
            izquierda += 1

    outputs.append(str(bebidas))

sys.stdout.write('\n'.join(outputs))