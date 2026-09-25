

def permutar(arreglo, inicio, fin):
    if inicio == fin:
        print(arreglo)
    
    else: 
        for i in range(inicio, fin+1):
            temp = arreglo[inicio]
            arreglo[inicio] = arreglo[i]
            arreglo[i] = temp
            permutar(arreglo, inicio+1, fin)
            temp = arreglo[inicio]
            arreglo[inicio] = arreglo[i]
            arreglo[i] = temp
            
# llamada inicial
arreglo = [1, 2, 3]
N = len(arreglo)
permutar(arreglo, 0, N-1)

########### ALTERNATIVA LIBRERIA PYTHON ############
from itertools import permutations

p = permutations(arreglo)

for element in p:
    print(element)
