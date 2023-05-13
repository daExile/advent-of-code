groups = []
n = 0
answers = open("06.txt", "r")
for line in answers:
    if line == "\n": n += 1
    else:
        if len(groups) == n:
            groups.append(line.strip())
        else: groups[n] += line.strip()

# ans_count = []
puzzle_answer = 0
for group in groups:
    puzzle_answer += len(set(group))
    
print("Answer:", puzzle_answer)
