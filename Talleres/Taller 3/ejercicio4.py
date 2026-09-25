import sys
from itertools import permutations


def es_heredero(numero):
    texto = str(numero)
    cantidad = len(texto)

    # La cantidad de dígitos debe ser par
    if cantidad % 2 != 0:
        return False

    mitad = cantidad // 2

    # Los padres tienen mitad de dígitos
    digitos = list(texto)

    # Evitamos probar dos veces la misma permutación
    candidatos = set(
        int("".join(p))
        for p in permutations(digitos, mitad)
        if p[0] != '0'
    )

    # Probamos todas las posibles parejas de padres
    for padre1 in candidatos:
        for padre2 in candidatos:
            if padre1 * padre2 != numero:
                continue

            # Verificamos que entre ambos padres estén
            # exactamente los mismos dígitos del heredero
            if sorted(str(padre1) + str(padre2)) == sorted(texto):
                return True

    return False


datos = list(map(int, sys.stdin.buffer.read().split()))
casos = datos[0]
resultados = []
for numero in datos[1:casos + 1]:
    if es_heredero(numero):
        resultados.append("Heredero")
    else:
        resultados.append("No")
sys.stdout.write("\n".join(resultados))


