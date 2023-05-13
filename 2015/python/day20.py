import math as m
my_input = int(input("Puzzle input: "))

def factorize(n):
    f = [n]
    for i in range(1, m.floor(m.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            f.append(q)
            f.append(i)
    return set(f)

max_p = 0
n = 0
while max_p < my_input:
    n += 1
    presents = sum(factorize(n)) * 10
    if max_p < presents:
        max_p = presents
        print("n = {}, {} presents".format(n, max_p))

print("Part 1 answer:", n)

def factorize_50(n):
    f = [n]
    for i in range(1, m.floor(m.sqrt(n)) + 1):
        q, r = divmod(n, i)
        if r == 0:
            f.append(q)
            f.append(i)
    a = list(set(f))
    a_50 = [x for x in a if x >= n / 50]
    return a_50

max_p = 0
n = 0
while max_p < my_input:
    n += 1
    presents = sum(factorize_50(n)[:50]) * 11
    if max_p < presents:
        max_p = presents
        print("n = {}, {} presents".format(n, max_p))

print("Part 2 answer:", n)
