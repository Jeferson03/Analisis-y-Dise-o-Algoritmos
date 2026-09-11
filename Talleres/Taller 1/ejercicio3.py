import sys

MOD = 49999
MAX = 100


def precompute():
    # answers[n][p] guarda:
    # 1^p + 2^p + ... + n^p (mod MOD)
    answers = [[0] * (MAX + 1) for _ in range(MAX + 1)]

    for p in range(1, MAX + 1):
        for n in range(1, MAX + 1):
            answers[n][p] = (
                answers[n - 1][p] + pow(n, p, MOD)
            ) % MOD

    return answers


def main():
    answers = precompute()

    input = sys.stdin.readline

    C = int(input())

    outputs = []

    for _ in range(C):
        N, P = map(int, input().split())

        outputs.append(str(answers[N][P]))

    sys.stdout.write('\n'.join(outputs))


main()