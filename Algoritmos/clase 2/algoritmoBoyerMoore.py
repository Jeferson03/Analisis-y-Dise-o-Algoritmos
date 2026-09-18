#Dado un arreglo X con N elementos enteros (aunque se puede extrapolar a otros tipos) determinar cuál, si es que lo hay, aparece más de N/2 veces

# complejidad algoritmica: O(N)
# complejidad en memoria: O(1)

def boyerMoore(X, N):
    conteo = 0
    for i in range (N):
        if conteo == 0:
            conteo = 1
            dominante = X[i]
        elif dominante == X[i]:
            conteo += 1
        else:
            conteo -= 1
    max_conteo = 0 
    for i in range(N):
        if X[i] == dominante:
            max_conteo += 1
    if max_conteo > N/2:
        print(dominante)
    else:
        print('NO')
    
arreglo = input().split(" ")
N = len(arreglo)

boyerMoore(arreglo, N)