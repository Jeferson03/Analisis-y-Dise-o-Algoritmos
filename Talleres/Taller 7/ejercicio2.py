
import sys

def resolver():
    datos = sys.stdin.read().split()
    S = int(datos[0])

    salida = []
    posicion = 1

    for _ in range(S):
        a = datos[posicion]
        b = datos[posicion + 1]
        posicion += 2

        # Usamos la secuencia más corta como columnas.
        if len(a) < len(b):
            a, b = b, a

        anterior = [0] * (len(b) + 1)

        for caracter_a in a:
            actual = [0] * (len(b) + 1)

            for j in range(1, len(b) + 1):
                if caracter_a == b[j - 1]:
                    actual[j] = anterior[j - 1] + 1
                else:
                    actual[j] = max(
                        anterior[j],
                        actual[j - 1]
                    )

            anterior = actual

        salida.append(str(anterior[len(b)]))

    sys.stdout.write("\n".join(salida))


resolver()
