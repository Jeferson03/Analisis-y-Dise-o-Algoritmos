# Dado un valor entero N mayor a 1, mostrar todos los números primos menores o iguales a N

#Paso 1: Crear una tabla con dos filas, en una poner los números enteros desde el 2 hasta el N y en la otra True
#
#Paso 2: El primer número de la tabla con valor True es primo
#
#Paso 3: Todos los múltiplos de ese número, a partir de su cuadrado, se ponen en False
#
#Paso 4: Si el cuadrado de ese número es menor que N se regresa al paso 2, encaso contario el algoritmo termina.
#
#Paso 5: Todos los números con valor True son los primos

# Complejidad algoritmica: O(N*log(log(N)))
# Complejidad en memoria: O(N)



def criba_eratostenes(N: int) -> list:
    es_primo = [True] * (N + 1)
    primos = []

    for i in range(2, N + 1):
        if es_primo[i]:
            primos.append(i)

            for j in range(i * i, N + 1, i):
                es_primo[j] = False

    return primos
            
            
N = int(input())
            
print(criba_eratostenes(N))
        
    
    
    
    