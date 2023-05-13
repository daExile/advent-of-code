import itertools
file = open("13.txt", "r")

h_scores = {}
for line in file:
    s = line.strip()
    n1, s = s.split(" would ")
    s, n2 = s[:-1].split(" happiness units by sitting next to ")
    pts = int(s[5:]) if s[:4] == "gain" else -int(s[5:])
    if n1 in h_scores: h_scores[n1][n2] = pts
    else: h_scores[n1] = {n2: pts}
file.close()

pepoles = list(h_scores.keys())
best_score = None
for c in itertools.permutations(pepoles, 8):
    score = 0
    c_l = list(c)
    for i in range(-1, 7):
        score += h_scores[c_l[i]][c_l[i-1]] + h_scores[c_l[i]][c_l[i+1]]
    if not best_score or score > best_score: best_score = score

print("Part 1 answer:", best_score)

for key in h_scores:
    h_scores[key]["me"] = 0
h_scores["me"] = {}
for pepole in pepoles:
    h_scores["me"][pepole] = 0

pepoles = list(h_scores.keys())
best_score = None
for c in itertools.permutations(pepoles, 9):
    score = 0
    c_l = list(c)
    for i in range(-1, 8):
        score += h_scores[c_l[i]][c_l[i-1]] + h_scores[c_l[i]][c_l[i+1]]
    if not best_score or score > best_score: best_score = score

print("Part 2 answer:", best_score)
