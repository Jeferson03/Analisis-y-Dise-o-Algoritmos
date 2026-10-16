import sys

input = sys.stdin.buffer.readline


class DSU:
    def __init__(self, n):
        self.padre = list(range(n + 1))
        self.tamano = [1] * (n + 1)
        self.componentes = n

    def encontrar(self, x):
        while self.padre[x] != x:
            self.padre[x] = self.padre[self.padre[x]]
            x = self.padre[x]
        return x

    def unir(self, a, b):
        a = self.encontrar(a)
        b = self.encontrar(b)

        if a == b:
            return False

        if self.tamano[a] < self.tamano[b]:
            a, b = b, a

        self.padre[b] = a
        self.tamano[a] += self.tamano[b]
        self.componentes -= 1
        return True


def resolver():
    datos = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0

    T = datos[pos]
    pos += 1

    salida = []

    for _ in range(T):
        N, M, A = datos[pos:pos + 3]
        pos += 3

        carreteras = []

        for _ in range(M):
            u, v, costo = datos[pos:pos + 3]
            pos += 3

            # Solo conviene incorporar carreteras más baratas que construir un aeropuerto
            if costo < A:
                carreteras.append((costo, u, v))

        carreteras.sort()

        dsu = DSU(N)
        costo_total = 0

        for costo, u, v in carreteras:
            if dsu.unir(u, v):
                costo_total += costo

        aeropuertos = dsu.componentes
        costo_total += aeropuertos * A

        salida.append(f"{costo_total} {aeropuertos}")

    sys.stdout.write("\n".join(salida))

resolver()
