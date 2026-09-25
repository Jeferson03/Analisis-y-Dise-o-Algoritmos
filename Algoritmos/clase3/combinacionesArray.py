

def combinar(base, N, arreglo):
    if len(arreglo) == N:
        print(arreglo)
        
    else:
        for element in base:
            new_array = arreglo.copy()
            new_array.append(element)
            combinar(base, N, new_array)
            
base = [0, 1]
N = len(base)
combinar(base, 4, [])


################## ALTERNATIVA LIBRERIA PYTHON ####################

from itertools import combinations

c = combinations(base, repeat=4) # repeat = N

for element in c:
    print(element)
