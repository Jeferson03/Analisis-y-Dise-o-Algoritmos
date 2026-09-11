import sys


LIMIT = 10**10


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def reverse_number(n):
    return int(str(n)[::-1])


def solve(n):

    # Si inicialmente ya es capicúa
    if is_palindrome(n):
        return "0"

    iterations = 0

    while True:

        reversed_n = reverse_number(n)

        n += reversed_n
        iterations += 1

        # Si alcanzamos el límite,
        # es sospechoso de Lychrel
        if n >= LIMIT:
            return "L"

        # Si llegamos a un capicúa
        if is_palindrome(n):
            return str(iterations)


def main():
    input = sys.stdin.readline

    outputs = []

    while True:
        n = int(input())

        if n == 0:
            break

        outputs.append(solve(n))

    sys.stdout.write('\n'.join(outputs))


main()