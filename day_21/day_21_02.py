import numpy as np
from tqdm import tqdm

from day_21.prepare_data import prepare_data


# def calculate_value(n):
#     # These magic numbers comes straight from reddit
#     a0, a1, a2 = 3906, 34896, 96784
#     b0, b1, b2 = a0, a1 - a0, a2 - a1
#     return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


def main():
    # This closely inspired from reddit in the goal to understand I don't deserve this star
    G = {(i + j * 1j): c for i, row in enumerate(open('data_challenge.txt'))
         for j, c in enumerate(row) if c in '.S'}

    N = 131

    done = []
    positions = {x for x in G if G[x] == 'S'}

    for s in range(int(2.5 * N) + 1):
        if s % N == N // 2:
            done.append(len(positions))

        positions = {p + d for d in {1, -1, 1j, -1j} for p in positions
                if (p + d).real % N + (p + d).imag % N * 1j in G}

    # something from reddit again
    f = lambda n, a, b, c: a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))

    print(f(26501365 // N, *done))


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")
