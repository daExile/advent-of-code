groups = []
n = 0
answers = open("06.txt", "r")
for line in answers:
    if line == "\n": n += 1
    else:
        if len(groups) == n:
            groups.append([])
        groups[n].append(line.strip())

answer = 0
for group in groups:
    answer += len(set("".join(group)))
    
print("Part 1:", answer)

answer = 0
for group in groups:
    size = len(group)   
    answers = ""
    for line in group:
        answers += line
    group_set = set(answers)
    eb_set = []
    for item in group_set:
        if answers.count(item) == size: eb_set.append(item)

    answer += len(eb_set)

print("Part 2:", answer)
