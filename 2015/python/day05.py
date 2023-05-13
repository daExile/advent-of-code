file = open("05.txt", "r")

def check_doubles(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]: return True
    return False

def check_double_pairs(s):
    for i in range(len(s) - 2):
        if s[i:i+2] in s[i+2:]: return True
    return False

def check_aba(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2]: return True
    return False

vtable = str.maketrans("aeiou", "00000")
r1_nice_cnt = 0
r2_nice_cnt = 0
for line in file:
    s = line.strip()

    #rule 1
    nice = False
    if not ("ab" in s or "cd" in s or "pq" in s or "xy" in s):
        if s.translate(vtable).count("0") > 2:
            if check_doubles(s): nice = True
    if nice:
        r1_nice_cnt += 1
        print("By 1st rule set", s, "is nice, #", r1_nice_cnt)

    #rule 2
    nice = False
    if check_double_pairs(s):
        if check_aba(s): nice = True
    
    if nice:
        r2_nice_cnt += 1
        print("By 2nd rule set", s, "is nice, #", r2_nice_cnt)
