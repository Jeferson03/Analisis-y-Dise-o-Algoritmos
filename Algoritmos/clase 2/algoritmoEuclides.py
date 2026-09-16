# Dados dos enteros positivos A y B, cuál es el mínimo valor que es múltiplo de ambos
# Se basa en:
#
#1) Al dividir M entre N, ambos números enteros, se obtiene un cociente Q más
#un residuo R
#2) El máximo común divisor de M y N es igual que el de N y R
#3) A*B = MinimoComunMultiplo(A, B) * MaximoComunDivisor(A, B)

A = int(input())
B = int(input())

M = A
N = B

while N != 0:
    temp = M
    M = N 
    N = temp%N
    
maxCD = M
minCM = (A*B)/maxCD
if minCM.is_integer():
    print(int(minCM))
else:
    print('NO')
    