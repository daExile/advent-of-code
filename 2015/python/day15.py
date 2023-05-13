import itertools
file = open("15.txt", "r")

stuff = {}
for line in file:
    s = line.strip()
    n, rest = s.split(": ")
    rest = rest.split(", ")
    stuff[n] = {}
    for item in rest:
        a, b = item.split()
        stuff[n][a] = int(b)
file.close()

ingreds = list(stuff.keys())
props = list(stuff[ingreds[0]].keys())

def get_score(setup, cal_max = 0):
    global props, ingreds, stuff
    c = [setup[0],
         setup[1] - setup[0] - 1,
         setup[2] - setup[1] - 1,
         102 - setup[2]]
    score = 1
    for p in props[0:4]:
        a = 0
        for i, ingred in enumerate(ingreds):
            a += c[i] * stuff[ingred][p]
        if a <= 0: return 0
        else: score *= a
    if cal_max <= 0: pass
    else:
        cal = 0
        for i, ingred in enumerate(ingreds):
            cal += c[i] * stuff[ingred]["calories"]
        if cal > cal_max: return 0
    return score

best_cookie_score = 0

best_diet_cookie_score = 0
calories = 500

snb_shit = list(range(103))
for setup in itertools.combinations(snb_shit, 3):
    score = get_score(setup)
    d_score = get_score(setup, calories)
    if best_cookie_score < score: best_cookie_score = score
    if best_diet_cookie_score < d_score: best_diet_cookie_score = d_score
print("Part 1 answer:", best_cookie_score)
print("Part 2 answer:", best_diet_cookie_score)
