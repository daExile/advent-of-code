pswd = list(input("Puzzle input: "))
alpha = "abcdefghijklmnopqrstuvwxyz"

def get_next(p, pos):
    p_new = p[:]
    if p_new[pos] == "z":
        p_new[pos] = "a"
        return(get_next(p_new, pos - 1))
    else:
        p_new[pos] = alpha[alpha.find(p_new[pos]) + 1]
        return p_new

def check_pairs(p):
    for i in range(len(p) - 3):
        if p[i] == p[i+1]:
            for j in range(i + 1, len(p) - 1):
                if p[j] == p[j+1] and p[j] != p[i]: return True
    return False

def check_threes(p):
    for i in range(len(p) - 2):
        if p[i] not in ["y", "z"]:
            if p[i+1] == alpha[alpha.find(p[i]) + 1]:
                if p[i+2] == alpha[alpha.find(p[i]) + 2]: return True
    return False

check = False
while not check:
    pswd = get_next(pswd, 7)[:]

    if not ("i" in pswd or "l" in pswd or "o" in pswd):
        if check_pairs(pswd):
            if check_threes(pswd): check = True

answer = ""
for letter in pswd: answer += letter
print("Part 1 answer:", answer)

check = False
while not check:
    pswd = get_next(pswd, 7)[:]

    if not ("i" in pswd or "l" in pswd or "o" in pswd):
        if check_pairs(pswd):
            if check_threes(pswd): check = True

answer = ""
for letter in pswd: answer += letter
print("Part 2 answer:", answer)
