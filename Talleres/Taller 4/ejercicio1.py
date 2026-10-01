import sys

input = lambda: sys.stdin.readline().strip()

denominaciones = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

N = int(input())
outputs = []

for _ in range(N):
    B = int(input())
    cantidad = 0

    for valor in denominaciones:
        cantidad += B // valor
        B %= valor

    outputs.append(str(cantidad))

sys.stdout.write('\n'.join(outputs))