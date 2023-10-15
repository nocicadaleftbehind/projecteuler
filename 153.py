import math

import tqdm


LIMIT = 10**8

# b = 0
sum_n = 0
for a in range(1, LIMIT + 1):
    sum_n += (LIMIT // a) * a

# b = a
for k in range(1, LIMIT // 2 + 1):
    sum_n += (LIMIT // (2 * k)) * 2 * k

# b > a
for a in tqdm.tqdm(range(1, LIMIT//2 + 1)):
    if 2 * a**2 > LIMIT:
        break

    for b in range(a + 1, LIMIT - a):
        gcd = math.gcd(a, b)
        if gcd > 1:
            continue

        norm = a ** 2 + b ** 2
        if norm > LIMIT:
            break
    
        for k in range(1, LIMIT // norm + 1):
            n2 = k * norm
            sum_n += ((gcd * LIMIT) // n2) * 2 * k * (a + b)

print()
print(sum_n)