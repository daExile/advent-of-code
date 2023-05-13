from itertools import combinations as combos

print("Puzzle input")
hp_b = int(input("Boss health: "))
dmg_b = int(input("Boss damage: "))
ar_b = int(input("Boss armor: "))
boss = (hp_b, dmg_b, ar_b)

weps = {"Dagger": (8, 4, 0),
        "Shortsword": (10, 5, 0),
        "Warhammer": (25, 6, 0),
        "Longsword": (40, 7, 0),
        "Greataxe": (74, 8, 0)}

armor = {"None": (0, 0, 0),
         "Leather": (13, 0, 1),
         "Chainmail": (31, 0, 2),
         "Splintmail": (53, 0, 3),
         "Bandedmail": (75, 0, 4),
         "Platemail": (102, 0, 5)}

rings = {"Damage +1": (25, 1, 0),
         "Damage +2": (50, 2, 0),
         "Damage +3": (100, 3, 0),
         "Defense +1": (20, 0, 1),
         "Defense +2": (40, 0, 2),
         "Defense +3": (80, 0, 3)}

r_list = list(combos(rings, 0)) + list(combos(rings, 1)) + list(combos(rings, 2))
print(r_list)

min_win = max_loss = None

def fight(player, boss):
    hp_p, dmg_p, ar_p = player
    hp_b, dmg_b, ar_b = boss

    while True:
        hp_b -= max(1, dmg_p - ar_b)
        if hp_b < 1: return True

        hp_p -= max(1, dmg_b - ar_p)
        if hp_p < 1: return False

for w in weps:
    for a in armor:
        for rs in r_list:
            dmg_p = weps[w][1]
            ar_p = armor[a][2]
            cost = weps[w][0] + armor[a][0]
            for r in rs:
                dmg_p += rings[r][1]
                ar_p += rings[r][2]
                cost += rings[r][0]

            if fight((100, dmg_p, ar_p), boss):
                print("Win for {} cost".format(cost))
                if not min_win or min_win > cost: min_win = cost
            else:
                print("Loss for {} cost".format(cost))
                if not max_loss or max_loss < cost: max_loss = cost

print("Part 1 answer:", min_win)
print("Part 2 answer:", max_loss)
