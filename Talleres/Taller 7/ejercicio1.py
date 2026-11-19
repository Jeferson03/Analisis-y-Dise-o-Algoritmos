
import sys

def resolver():
    lineas = sys.stdin.read().strip().splitlines()
    C = int(lineas[0])

    salida = []

    for i in range(1, C + 1):
        valores = list(map(int, lineas[i].split()))

        M = valores[0]
        denominaciones = valores[1:]

        INF = float("inf")
        dp = [INF] * (M + 1)
        dp[0] = 0

        for cantidad in range(1, M + 1):
            for d in denominaciones:
                if d > cantidad:
                    break

                dp[cantidad] = min(
                    dp[cantidad],
                    dp[cantidad - d] + 1
                )

        salida.append(str(dp[M]))

    sys.stdout.write("\n".join(salida))


resolver()
