import json
import sys
from tqdm import tqdm

sys.set_int_max_str_digits(0)

with open("data/settings.json", "r") as f:
    settings = json.load(f)
    n = settings["n"]

with open("data/primes.json", "r") as f:
    primes = json.load(f)

with open("data/relations.json", "r") as f:
    relations = json.load(f)

vecs = []

for relation in tqdm(relations):
    a, b = relation, relation**2 % n

    c = b
    vec = {}

    for p in primes:
        while c % p == 0:
            if p not in vec:
                vec[p] = False

            c //= p

            vec[p] = not vec[p]

        if c == 1:
            break

    _vec = vec
    vec = []
    for k, v in _vec.items():
        if v:
            vec.append(k)

    vecs.append(vec)

print(f"Matrix size: {len(vecs)}x{len(primes)}")

matrix = []
for vec in vecs:
    line = 0

    for p in vec:
        i = primes.index(p)
        line |= 1 << i

    matrix.append(line)

with open("data/matrix.json", "w") as f:
    json.dump(matrix, f)
