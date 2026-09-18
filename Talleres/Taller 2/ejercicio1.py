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
    divisores = 2
    raiz = math.isqrt(N)
    
    for i in range(2, raiz+1):
        
        if (N % i) == 0:
            
            if  N//i == i:
                divisores += 1
                
            else:
                divisores += 2
    
    outputs.append(str(divisores))
    
sys.stdout.write('\n'.join(outputs))
            
