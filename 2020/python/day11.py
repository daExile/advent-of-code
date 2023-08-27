def sit_check(seats, row, col, p2):
    occ = 0
    if not p2:
        for a in range(row - 1, row + 2):
            for b in range(col - 1, col + 2):
                if a >= 0 and a < len(seats) and b >= 0 and b < len(seats[row]):
                    if seats[a][b] == "#":
                        occ += 1
        return occ
    else:
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                crow = row + a
                ccol = col + b
                while crow >= 0 and crow < len(seats) and ccol >= 0 and ccol < len(seats[row]):
                    if seats[crow][ccol] == ".":
                        crow = crow + a
                        ccol = ccol + b
                    elif seats[crow][ccol] == "#":
                        occ += 1
                        break
                    else: break
        return occ

def leave_check(seats, row, col, p2):
    occ = 0
    if not p2:
        for a in range(row - 1, row + 2):
            for b in range(col - 1, col + 2):
                if a >= 0 and a < len(seats) and b >= 0 and b < len(seats[row]):
                    if seats[a][b] == "#":
                        occ += 1
        return occ - 1
    else:
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                crow = row + a
                ccol = col + b
                while crow >= 0 and crow < len(seats) and ccol >= 0 and ccol < len(seats[row]):
                    if seats[crow][ccol] == ".":
                        crow = crow + a
                        ccol = ccol + b
                    elif seats[crow][ccol] == "#":
                        occ += 1
                        break
                    else: break                
        return occ - 1

seats = []
seatmap = open("11.txt", "r")
for row in seatmap:
    seats.append(row.strip())
seatmap.close()

def simulate(seats, p2):
    changes = 1 # i guess, for the start
    rounds = 0
    leave_threshold = 5 if p2 else 4
    while changes:
        changes = 0
        seats_new = []
        for row in range(0, len(seats)):
            row_new = ""
            for col in range(0, len(seats[row])):
                if seats[row][col] == ".":
                    row_new += "."
                elif seats[row][col] == "L":
                    chk = sit_check(seats, row, col, p2)
                    if chk > 0: row_new += "L"
                    else:
                        row_new += "#"
                        changes += 1
                elif seats[row][col] == "#":
                    chk = leave_check(seats, row, col, p2)
                    if chk < leave_threshold: row_new += "#"
                    else:
                        row_new += "L"
                        changes += 1
            seats_new.append(row_new)
            
        if changes:
            rounds += 1
            seats = seats_new

    else:
        taken = 0
        for row in seats: taken += row.count("#")
    return taken

print("Part 1:", simulate(seats[:], False))
print("Part 2:", simulate(seats[:], True))
