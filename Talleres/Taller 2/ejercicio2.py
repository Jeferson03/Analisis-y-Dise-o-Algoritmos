import sys
import math

input = lambda: sys.stdin.readline().strip()

C = int(input())
outputs = []

for _ in range(C):
    periodos = list(map(int, input().split()))

    mcm = periodos[0]

    for periodo in periodos[1:]:
        mcm = (mcm * periodo) // math.gcd(mcm, periodo)

    outputs.append(str(mcm))

sys.stdout.write('\n'.join(outputs))
    
    