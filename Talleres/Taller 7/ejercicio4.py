
import sys

def lcs(a, b):
    anterior = [0] * (len(b) + 1)

    for i in range(1, len(a) + 1):
        actual = [0] * (len(b) + 1)

        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                actual[j] = anterior[j - 1] + 1
            else:
                actual[j] = max(anterior[j], actual[j - 1])

        anterior = actual

    return anterior[-1]


def resolver():
    lineas = sys.stdin.read().strip().splitlines()
    C = int(lineas[0])
    pos = 1
    salida = []

    for caso in range(1, C + 1):
        E = int(lineas[pos])
        pos += 1

        correcta = list(map(int, lineas[pos].split()))
        pos += 1

        N = len(correcta)

        salida.append(f"caso {caso}:")

        for _ in range(E):
            respuesta = list(map(int, lineas[pos].split()))
            pos += 1

            puntos = lcs(correcta, respuesta)
            nota = (puntos * 100 * 2 + N) // (2 * N)

            salida.append(str(nota))

        if caso < C:
            salida.append("")

    sys.stdout.write("\n".join(salida))



resolver()

