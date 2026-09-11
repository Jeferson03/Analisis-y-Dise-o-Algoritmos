import sys


def is_kaprekar(n):
    # El enunciado exige que sea mayor que 3
    if n <= 3:
        return False

    square = n * n
    divisor = 10

    # Probamos todas las posibles divisiones del cuadrado
    while divisor <= square:

        right = square % divisor
        left = square // divisor

        # El segundo sumando no puede ser nulo
        if right != 0 and left + right == n:
            return True

        divisor *= 10

    return False


def main():
    input = sys.stdin.readline

    C = int(input())

    outputs = []

    for _ in range(C):
        n = int(input())

        if is_kaprekar(n):
            outputs.append("KAP")
        else:
            outputs.append("NO")

    sys.stdout.write('\n'.join(outputs))


main()