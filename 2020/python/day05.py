allaboard = []
max_id = 0
min_id = 1024
board_data = open("05.txt", "r")
for line in board_data:
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("L", "0")
    line = line.replace("R", "1")
    cur_id = int(line, 2)
    if cur_id > max_id: max_id = cur_id
    if cur_id < min_id: min_id = cur_id
    allaboard.append(cur_id)

print("Part 1:", max_id)

for a in range(min_id + 1, max_id):
    if a not in allaboard:
        print("Part 2:", a)
        break
