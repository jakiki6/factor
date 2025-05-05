import json
import math
import os
from tqdm import tqdm

with open("data/settings.json", "r") as f:
    settings = json.load(f)
    n = settings["n"]
    s = settings["s"]

with open("data/primes.json", "r") as f:
    primes = json.load(f)

relations = []
if os.path.isfile("data/relations.json"):
    with open("data/relations.json", "r") as f:
        relations = json.load(f)

print(f"Factoring {n}")

needed = int(s / math.log(s))
print(f"I need {needed} relations, have {len(relations)}")

a = math.isqrt(n) + 1

have = len(relations)
if have:
    a = relations[-1] + 1

try:
    for i in tqdm(range(0, needed)):
        if i < have:
            continue

        relation = None
        while relation is None:
            b = pow(a, 2, n)
            if a == b or b == 0:
                continue

            c = b
            vec = []
            for p in primes:
                while c % p == 0:
                    if p in vec:
                        vec.remove(p)
                    else:
                        vec.append(p)

                    c //= p

                if c == 1:
                    break

            if c == 1 and a not in relations and len(vec):
                relation = a

            a += 1

        relations.append(relation)
finally:
    with open("data/relations.json", "w") as f:
        json.dump(relations, f)
