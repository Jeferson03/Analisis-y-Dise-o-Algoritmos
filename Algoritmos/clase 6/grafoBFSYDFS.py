from collections import deque


class Grafo:
    """Grafo dirigido y ponderado mediante lista de adyacencia."""

    def __init__(self) -> None:
        self._adyacencia: dict[str, dict[str, float]] = {}

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self._adyacencia:
            self._adyacencia[vertice] = {}

    def agregar_arista(
        self, origen: str, destino: str, peso: float
    ) -> None:
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self._adyacencia[origen][destino] = peso

    def eliminar_arista(self, origen: str, destino: str) -> None:
        if origen in self._adyacencia:
            self._adyacencia[origen].pop(destino, None)

    def eliminar_vertice(self, vertice: str) -> None:
        if vertice not in self._adyacencia:
            return

        del self._adyacencia[vertice]

        for vecinos in self._adyacencia.values():
            vecinos.pop(vertice, None)

    def contiene_vertice(self, vertice: str) -> bool:
        return vertice in self._adyacencia

    def contiene_arista(self, origen: str, destino: str) -> bool:
        return (
            origen in self._adyacencia
            and destino in self._adyacencia[origen]
        )

    def obtener_vecinos(self, vertice: str) -> dict[str, float]:
        if vertice not in self._adyacencia:
            raise KeyError(f"El vértice {vertice!r} no existe")
        return self._adyacencia[vertice].copy()

    def vertices(self) -> list[str]:
        return list(self._adyacencia)

    def cantidad_vertices(self) -> int:
        return len(self._adyacencia)

    def cantidad_aristas(self) -> int:
        return sum(
            len(vecinos)
            for vecinos in self._adyacencia.values()
        )

    def __str__(self) -> str:
        lineas = []

        for vertice, vecinos in self._adyacencia.items():
            conexiones = ", ".join(
                f"{destino} (peso={peso})"
                for destino, peso in vecinos.items()
            )
            lineas.append(f"{vertice} -> [{conexiones}]")

        return "\n".join(lineas)


def bfs(grafo: Grafo, inicio: str) -> list[str]:
    """Recorrido en anchura."""
    if not grafo.contiene_vertice(inicio):
        raise KeyError(f"El vértice {inicio!r} no existe")

    visitados = {inicio}
    cola = deque([inicio])
    recorrido = []

    while cola:
        actual = cola.popleft()
        recorrido.append(actual)

        for vecino in grafo.obtener_vecinos(actual):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

    return recorrido


def dfs(grafo: Grafo, inicio: str) -> list[str]:
    """Recorrido en profundidad iterativo."""
    if not grafo.contiene_vertice(inicio):
        raise KeyError(f"El vértice {inicio!r} no existe")

    visitados = set()
    pila = [inicio]
    recorrido = []

    while pila:
        actual = pila.pop()

        if actual in visitados:
            continue

        visitados.add(actual)
        recorrido.append(actual)

        vecinos = list(grafo.obtener_vecinos(actual))

        for vecino in reversed(vecinos):
            if vecino not in visitados:
                pila.append(vecino)

    return recorrido


#def main() -> None:
#    grafo = Grafo()
#
#    # Construir el grafo.
#    grafo.agregar_arista("A", "B", 4)
#    grafo.agregar_arista("A", "D", 2)
#    grafo.agregar_arista("B", "C", 3)
#    grafo.agregar_arista("B", "E", 5)
#    grafo.agregar_arista("D", "E", 1)
#    grafo.agregar_vertice("F")  # Vértice aislado.
#
#    print("=== GRAFO ===")
#    print(grafo)
#
#    print("\n=== INFORMACIÓN ===")
#    print("Vértices:", grafo.vertices())
#    print("Cantidad de vértices:", grafo.cantidad_vertices())
#    print("Cantidad de aristas:", grafo.cantidad_aristas())
#
#    print("\n=== RECORRIDOS DESDE A ===")
#    print("BFS:", bfs(grafo, "A"))
#    print("DFS:", dfs(grafo, "A"))
#
#    print("\n=== CONSULTAS ===")
#    print("¿Existe A -> B?", grafo.contiene_arista("A", "B"))
#    print("¿Existe B -> A?", grafo.contiene_arista("B", "A"))
#    print("Vecinos de A:", grafo.obtener_vecinos("A"))
#
#    print("\n=== MODIFICACIÓN ===")
#    grafo.eliminar_arista("A", "B")
#    print("¿Existe A -> B después de eliminarla?",
#          grafo.contiene_arista("A", "B"))
#
#
#if __name__ == "__main__":
#    main()
#