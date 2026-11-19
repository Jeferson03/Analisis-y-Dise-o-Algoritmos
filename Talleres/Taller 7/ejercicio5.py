
import sys

def palindromizar(s):
    n = len(s)

    dp = [[0] * n for _ in range(n)]

    # longitud del fragmento
    for longitud in range(2, n + 1):

        for i in range(n - longitud + 1):
            j = i + longitud - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                insertar = dp[i][j - 1]
                eliminar = dp[i + 1][j]
                reemplazar = dp[i + 1][j - 1]

                dp[i][j] = 1 + min(
                    insertar,
                    eliminar,
                    reemplazar
                )

    return dp[0][n - 1]


def resolver():
    datos = sys.stdin.read().split()
    N = int(datos[0])

    salida = []

    for i in range(1, N + 1):
        s = datos[i]
        salida.append(str(palindromizar(s)))

    sys.stdout.write("\n".join(salida))



resolver()
