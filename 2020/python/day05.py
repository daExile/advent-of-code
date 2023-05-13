allaboard = []
max_id = 0
min_id = 1024
board_data = open("05.txt", "r")
for line in board_data:
    line = line.replace("F", "0")
    line = line.replace("B", "1")
    line = line.replace("L", "0")
    line = line.replace("R", "1")
    # print(int(line, 2))
    if int(line, 2) > max_id: max_id = int(line, 2)

print(max_id)
