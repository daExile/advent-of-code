file = open("02.txt", "r")

score = 0
for line in file:
    s = line.strip().split()
    if s[1] == "X":
        if s[0] == "A": score += 3
        elif s[0] == "B": score += 1
        elif s[0] == "C": score += 2

    if s[1] == "Y":
        if s[0] == "A": score += 4
        elif s[0] == "B": score += 5
        elif s[0] == "C": score += 6

    if s[1] == "Z":
        if s[0] == "A": score += 8
        elif s[0] == "B": score += 9
        elif s[0] == "C": score += 7
    #if s[0] == "A" and s[1] == "Y": score += 6
    #elif s[0] == "B" and s[1] == "Z": score += 6
    #elif s[0] == "C" and s[1] == "X": score += 6
    #elif s[0] == "A" and s[1] == "X": score += 3
    #elif s[0] == "B" and s[1] == "Y": score += 3
    #elif s[0] == "C" and s[1] == "Z": score += 3

    #if s[1] == "X": score += 1
    #elif s[1] == "Y": score += 2
    #elif s[1] == "Z": score += 3

print(score)
