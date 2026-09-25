import sys

input = lambda: sys.stdin.readline().strip()

# Tabla de verificación del DNI español
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

C = int(input())
outputs = []

for _ in range(C):
    dni = input()

    # Encontrar las posiciones desconocidas
    posiciones = []

    for i in range(8):
        if dni[i] == '?':
            posiciones.append(i)

    compatibles = 0

    # Cantidad de combinaciones posibles
    total = 10 ** len(posiciones)

    for numero in range(total):

        # Convertimos el número de combinación a dígitos
        valor = numero

        digitos = list(dni)

        # Rellenar los '?'
        for pos in reversed(posiciones):
            digitos[pos] = str(valor % 10)
            valor //= 10

        # Construir los 8 dígitos
        numero_dni = int(''.join(digitos[:8]))

        # Calcular letra de verificación
        letra = letras[numero_dni % 23]

        # Comprobar si coincide
        if letra == dni[8]:
            compatibles += 1

    outputs.append(str(compatibles))

sys.stdout.write('\n'.join(outputs))

