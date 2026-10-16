import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()


class Nodo:

    def __init__(self, frecuencia, caracter=None,
                 izquierda=None, derecha=None):

        self.frecuencia = frecuencia
        self.caracter = caracter
        self.izquierda = izquierda
        self.derecha = derecha

        if caracter is not None:
            self.clave = caracter
        else:
            self.clave = min(izquierda.clave, derecha.clave)

    def __lt__(self, otro):

        if self.frecuencia != otro.frecuencia:
            return self.frecuencia < otro.frecuencia

        return self.clave < otro.clave

    def es_hoja(self):
        return self.caracter is not None


def construir_arbol(caracteres):

    heap = []

    for caracter, frecuencia in caracteres:
        nodo = Nodo(frecuencia, caracter)
        heapq.heappush(heap, nodo)

    while len(heap) > 1:

        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)

        nuevo = Nodo(
            izquierda.frecuencia + derecha.frecuencia,
            izquierda=izquierda,
            derecha=derecha
        )

        heapq.heappush(heap, nuevo)

    return heap[0]


def obtener_codigos(nodo, codigo="", resultado=None):

    if resultado is None:
        resultado = {}

    if nodo.es_hoja():
        resultado[nodo.caracter] = codigo
        return resultado

    obtener_codigos(
        nodo.izquierda,
        codigo + "0",
        resultado
    )

    obtener_codigos(
        nodo.derecha,
        codigo + "1",
        resultado
    )

    return resultado


def inorder(nodo, resultado):

    if nodo is None:
        return

    inorder(nodo.izquierda, resultado)

    if nodo.es_hoja():
        resultado.append(nodo.caracter)

    inorder(nodo.derecha, resultado)


T = int(input())

salida = []

for caso in range(1, T + 1):

    N = int(input())

    caracteres = []

    for _ in range(N):
        caracter, frecuencia = input().split()
        frecuencia = int(frecuencia)

        caracteres.append((caracter, frecuencia))

    raiz = construir_arbol(caracteres)

    codigos = obtener_codigos(raiz)

    orden = []
    inorder(raiz, orden)

    salida.append(f"caso {caso}:")

    for caracter in orden:
        salida.append(f"{caracter} {codigos[caracter]}")

    if caso != T:
        salida.append("")

sys.stdout.write("\n".join(salida))