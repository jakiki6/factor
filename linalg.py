import json
import math

with open("data/settings.json", "r") as f:
    settings = json.load(f)
    n = settings["n"]

with open("data/primes.json", "r") as f:
    primes = json.load(f)

with open("data/relations.json", "r") as f:
    relations = json.load(f)

with open("data/matrix.json", "rb") as f:
    matrix = json.load(f)


def generate_candidates():
    B = max(matrix).bit_length()
    basis = [0] * B
    basis_idx = [set() for _ in range(B)]

    for i, v in enumerate(matrix):
        x = v
        idx_set = {i}
        for b in reversed(range(B)):
            if not (x >> b) & 1:
                continue
            if basis[b]:
                x ^= basis[b]
                idx_set ^= basis_idx[b]
            else:
                basis[b] = x
                basis_idx[b] = idx_set.copy()
                break
        else:
            yield idx_set


for indexes in generate_candidates():
    a = 1
    b = 1

    for i in indexes:
        a = (a * relations[i]) % n
        b = b * (relations[i] ** 2 % n)

    b = math.isqrt(b)

    p = math.gcd(a + b, n)
    q = math.gcd(b - a, n)

    if p != 1 and q != 1 and p * q == n:
        print(p, q)

        exit(0)

print("No factors found :(")
