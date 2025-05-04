import json
import os

n = int(input("n: "))
smoothness = int(input("s: "))

if not os.path.isdir("data"):
    os.mkdir("data")

with open("data/settings.json", "w") as f:
    json.dump({"n": n, "s": smoothness}, f)

sieve = [False for _ in range(0, smoothness)]
primes = []

for i in range(2, smoothness):
    if sieve[i]:
        continue
    else:
        primes.append(i)

        j = i
        while j < smoothness:
            sieve[j] = True
            j += i

with open("data/primes.json", "w") as f:
    json.dump(primes, f)
