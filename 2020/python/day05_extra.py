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

print("Seat IDs range is:", min_id, "-", max_id)

# yeah we skip the upper bound itself cuz we know it's not the answer
# we're also lazy as fuck and ain't doing min_id + 1, deal with it
for a in range(min_id, max_id):
    if a not in allaboard:
        print("Our vacant seat ID:", a)
        break
