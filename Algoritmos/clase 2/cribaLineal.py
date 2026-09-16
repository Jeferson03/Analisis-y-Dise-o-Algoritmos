# Tambien llamada criba de Euler
# complejidad algoritmica: O(N)
# complejidad en memoria: O(N)

def criba_lineal(N):
    es_primo = [True for _ in range(N+1)]
    primos = []
    for i in range(2, N):
        if es_primo[i]:
            primos.append(i)
        for p in primos:
            if p*i > N:
                break
            es_primo[p*i] = False
            if ((i%p) == 0):
                break
    return primos

N = int(input())

print(criba_lineal(N))