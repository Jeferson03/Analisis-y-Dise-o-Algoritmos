import sys
from functools import cmp_to_key

input = lambda: sys.stdin.readline().strip()


def comparar(a, b):
    """ Recibe dos tuplas de dos valores y hace una comparacion para saber cual tiene más prioridad"""
    # a = (tiempo, multa)
    # b = (tiempo, multa)

    izquierda = a[0] * b[1]
    derecha = b[0] * a[1]

    if izquierda < derecha:
        return -1
    elif izquierda > derecha:
        return 1
    else:
        return 0


C = int(input())
outputs = []

for _ in range(C):

    N = int(input())

    trabajos = []

    for _ in range(N):
        tiempo, multa = map(int, input().split())
        trabajos.append((tiempo, multa))

    trabajos.sort(key=cmp_to_key(comparar))

    tiempo_acumulado = 0
    penalizacion = 0

    for tiempo, multa in trabajos:
        penalizacion += tiempo_acumulado * multa
        tiempo_acumulado += tiempo

    outputs.append(str(penalizacion))

sys.stdout.write('\n'.join(outputs))