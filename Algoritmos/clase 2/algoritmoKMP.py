#Dado un patrón P de tamaño M, encontrar en qué índices aparece dentro un texto T de tamaño N (M ≤ N).

# complejidad algoritmica: O(N + M)
# complejidad en memoria: O()

def calcular_lps(P, M):    
    LPS = [0] * M #arreglo de tamano M 
    LPS[0] = 0
    len = 0 #longitud sufijo-prefijo mas largo actual
    j = 1
    
    while j < M:
        if P[j] == P[len]:
            len += 1
            LPS[j] = len
            j += 1
            
        else:
            if len != 0:
                len = LPS[len-1]
                
            else:
                LPS[j] = 0
                j += 1
                
    return LPS
            
  

def KMP(T, P):
    N = len(T)
    M = len(P)
    LPS = calcular_lps(P, M)
    i = 0
    j = 0
    
    while i < N:
        if T[i] == P[j]:
            i += 1
            j += 1
            
            if j == M:
                print(i-j) # imprimimos el indice de la coincidencia (donde empieza)
                j = LPS[j-1]
                
        else:
            if j != 0:
                j = LPS[j-1]
                
            else:
                i += 1
        

T = input()        
P = input()

KMP(T, P)