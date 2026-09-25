from itertools import permutations


def contar_organizaciones(n, numeros):
    respuesta = 0

    # Los tres vértices están ordenados:
    # A, B y C representan posiciones diferentes.
    for A, B, C in permutations(numeros, 3):

        restantes = [x for x in numeros if x != A and x != B and x != C]

        # Suma que deben tener las parejas de cada lado
        suma_ab = n - A - B
        suma_bc = n - B - C
        suma_ca = n - C - A

        # Encontramos todas las parejas posibles de los 6 números
        parejas = []

        for i in range(6):
            for j in range(i + 1, 6):
                if restantes[i] + restantes[j] in (
                    suma_ab, suma_bc, suma_ca
                ):
                    parejas.append((i, j, restantes[i] + restantes[j]))

        # Buscamos una pareja para cada lado
        for p1 in parejas:
            i1, j1, s1 = p1

            if s1 != suma_ab:
                continue

            usados1 = {i1, j1}

            for p2 in parejas:
                i2, j2, s2 = p2

                if s2 != suma_bc:
                    continue

                usados2 = {i2, j2}

                # Las dos parejas no pueden compartir números
                if usados1 & usados2:
                    continue

                # Los dos números restantes forman el tercer lado
                restantes_indices = set(range(6)) - usados1 - usados2

                if len(restantes_indices) != 2:
                    continue

                i3, j3 = restantes_indices

                if restantes[i3] + restantes[j3] != suma_ca:
                    continue

                # Cada una de las tres parejas puede intercambiar
                # sus elementos: 2 * 2 * 2 = 8
                respuesta += 8

    return respuesta


# Entrada
C = int(input())

for _ in range(C):
    datos = list(map(int, input().split()))

    n = datos[0]
    numeros = datos[1:]

    print(contar_organizaciones(n, numeros))