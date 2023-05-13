file = open("14.txt", "r")

deers = {}
for line in file:
    s = line.strip()
    n, _, _, spd, _, _, tfly, _, _, _, _, _, _, trest, _ = s.split()
    deers[n] = {"spd": int(spd), "tfly": int(tfly), "trest": int(trest)}
file.close()

race_time = 2503

def distance(deer, t):
    runs, rem = divmod(t, deer["tfly"] + deer["trest"])
    dist = runs * deer["tfly"] * deer["spd"]
    extra_time = deer["tfly"] if rem >= deer["tfly"] else rem
    dist += deer["spd"] * extra_time
    return dist

print("Part 1 race results:")
results = []
for deer in deers:
    d = distance(deers[deer], race_time)
    results.append((deer, d))

results.sort(key = lambda item: item[1], reverse=True)
for i, deer in enumerate(results):
    print("{}. {:<7s} - {:>4}".format(i+1, deer[0], deer[1]))

#dumb "bruteforce" calc for part 2
standings = {}
for deer in deers: standings[deer] = 0
for t in range(1, race_time + 1):
    results = []
    for deer in deers:
        d = distance(deers[deer], t)
        results.append([deer, d])
    p1 = max(results, key = lambda item: item[1])
    for deer in results:
        if deer[1] == p1[1]: standings[deer[0]] = standings[deer[0]] + 1
results = list(standings.items())
results.sort(key = lambda item: item[1], reverse=True)

print("\nPart 2 race results:")
for i, deer in enumerate(results):
    print("{}. {:<7s} - {:>4}".format(i+1, deer[0], deer[1]))
