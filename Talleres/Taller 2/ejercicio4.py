import sys
from math import gcd

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

respuestas = []

for _ in range(N):
    a, b, c = map(int, input().split())

    mcd = gcd(gcd(a, b), c)

    tamaño = (a + b + c) // mcd

    respuestas.append(str(tamaño))

sys.stdout.write("\n".join(respuestas))