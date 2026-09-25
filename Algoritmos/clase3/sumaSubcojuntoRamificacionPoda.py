import numpy as np

def combinar(base, N, arreglo):
    M = len(arreglo)
    if M == N and np.dot(arreglo, X) == T:
        print(arreglo)
    else:
        for element in base:
            new_array = arreglo.copy()
            new_array.append(element)
            actual_sum = np.dot(new_array, X)
            remaining = sum(X[M:])
            if actual_sum == T:
                # poda por suficiencia 
                pass
            elif actual_sum > T:
                # poda por exceso
                pass
            elif actual_sum + remaining < T:
                # poda por insuficiencia
                pass
            else: 
                combinar(base, N, new_array)  
        
        

X = [80, 30, 50, 40, 10, 20] # arreglo ingresado por el usuario
T = 70 # Valor condicional
N = len(X)
base = [0, 1]
combinar(base, N, [])