import sys

input = lambda: sys.stdin.readline().strip()

C = int(input())
outputs = []

for _ in range(C):

    F = int(input())

    dias = {
        "sabado": [],
        "domingo": [],
        "lunes": []
    }

    for _ in range(F):
        dia, hora, duracion = input().split()

        h, m = map(int, hora.split(":"))

        inicio = h * 60 + m
        fin = inicio + int(duracion)

        # Gordie solo puede atender entre 06:00 y 24:00
        if inicio >= 6 * 60 and fin <= 24 * 60:
            dias[dia].append((fin, inicio))

    total = 0

    for dia in dias:

        # Ordenar por hora de finalización
        dias[dia].sort()

        ultimo_fin = 6 * 60

        for fin, inicio in dias[dia]:

            if inicio >= ultimo_fin:
                total += 1
                ultimo_fin = fin

    outputs.append(str(total))

sys.stdout.write('\n'.join(outputs))