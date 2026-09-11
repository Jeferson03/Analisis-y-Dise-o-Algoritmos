import sys
import math

input = lambda: sys.stdin.readline().rstrip()

# Cantidad de casos
C = int(input())

# Guardar todas las respuestas
outputs = []

# Resolver cada caso
for _ in range(C):

    N = int(input())

    # Usar división normal para trabajar con float
    valor = (N * N + N) / 2

    # Calcular raíz cuadrada
    casa = math.sqrt(valor)

    # Si Python la considera un entero
    if casa.is_integer():
        outputs.append(str(int(casa)))
    else:
        outputs.append("NO")

# Imprimir todas las respuestas juntas
sys.stdout.write("\n".join(outputs))