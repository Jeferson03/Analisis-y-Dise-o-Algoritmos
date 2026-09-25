import sys
from itertools import permutations


def costo_minimo(distancias, ciudades):
    mejor = float("inf")

    for ruta in permutations(range(ciudades)):
        distancia_total = 0
        posible = True

        for i in range(ciudades - 1):
            distancia = distancias[ruta[i]][ruta[i + 1]]

            if distancia is None:
                posible = False
                break

            distancia_total += distancia

        if posible:
            mejor = min(mejor, distancia_total)

    if mejor == float("inf"):
        return "imposible"

    # El costo es distancia / 10
    # Se redondea al entero más cercano.
    return str(round(mejor / 10))


entrada = sys.stdin.buffer
casos = int(entrada.readline())
resultados = []
for _ in range(casos):
    ciudades = int(entrada.readline())
    distancias = []
    for _ in range(ciudades):
        fila = entrada.readline().split()
        distancias.append([
            None if valor == b"n.a" else int(valor)
            for valor in fila
        ])
    resultados.append(
        costo_minimo(distancias, ciudades)
    )
sys.stdout.write("\n".join(resultados))

