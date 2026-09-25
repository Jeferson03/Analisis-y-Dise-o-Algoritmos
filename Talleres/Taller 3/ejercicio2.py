import sys


def tiempo_sobrante(M, canciones):
    dp = [False] * (M + 1)
    dp[0] = True

    for duracion in canciones:
        for tiempo in range(M, duracion - 1, -1):
            dp[tiempo] = dp[tiempo] or dp[tiempo - duracion]

    for tiempo in range(M, -1, -1):
        if dp[tiempo]:
            return M - tiempo



entrada = sys.stdin.buffer
casos = int(entrada.readline())
resultados = []
for _ in range(casos):
    datos = list(map(int, entrada.readline().split()))
    M = datos[0]
    canciones = datos[1:]
    resultados.append(str(tiempo_sobrante(M, canciones)))
sys.stdout.write("\n".join(resultados))


