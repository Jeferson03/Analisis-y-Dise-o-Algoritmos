import sys


def solve(M):
    # 1² + 2² + ... + M²
    total = M * (M + 1) * (2 * M + 1) // 6

    count = 0

    # Para S = 3:
    # izquierda = 1² + 2² = 5
    left = 5

    for S in range(3, M):

        # Derecha = total - izquierda - S²
        right = total - left - S * S

        # La suma derecha debe ser múltiplo
        # de la suma izquierda.
        if right % left == 0:
            count += 1

        # Para la siguiente posición S+1,
        # S² pasa a formar parte de la izquierda.
        left += S * S

    return count


def main():
    data = map(int, sys.stdin.buffer.read().split())

    outputs = []

    # Si un mismo M aparece varias veces,
    # evitamos recalcularlo.
    cache = {}

    for M in data:
        if M == 0:
            break

        if M not in cache:
            cache[M] = solve(M)

        outputs.append(str(cache[M]))

    sys.stdout.write('\n'.join(outputs))
    
main()