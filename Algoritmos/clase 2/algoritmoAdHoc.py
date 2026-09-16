# Dado un valor entero positivo N, mostrar todos sus divisores diferentes de 1 y N
import math
N = int(input())

raiz = math.isqrt(N)
for i in range(2, N):
    if N%i == 0:
        if i != raiz:
            print(str(i) + " " + str(N//i))
        else:
            print(i)
            
# complejidad algoritmica: O(sqrt(n)) 