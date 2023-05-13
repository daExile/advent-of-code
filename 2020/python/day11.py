def sit_check(seats, row, col):
    occ = 0
    for a in range(row - 1, row + 2):
        for b in range(col - 1, col + 2):
            if a >= 0 and a < len(seats) and b >= 0 and b < len(seats[row]):
                if seats[a][b] == "#":
                    occ += 1
    return occ

def leave_check(seats, row, col):
    # print("Checking (", row, ",", col, ")")
    occ = 0
    for a in range(row - 1, row + 2):
        for b in range(col - 1, col + 2):
            if a >= 0 and a < len(seats) and b >= 0 and b < len(seats[row]):
                if seats[a][b] == "#":
                    occ += 1
                # print(a, b, seats[a][b], occ)
            # else: print(a, b, "X", occ)
    return occ - 1

seats = []
seatmap = open("11.txt", "r")
for row in seatmap:
    seats.append(row.strip())
seatmap.close()

changes = 1 # i guess, for the start
rounds = 0
while changes:
    changes = 0
    seats_new = []
    # seat_checks = []
    for row in range(0, len(seats)):
        row_new = ""
        # check_row = ""
        for col in range(0, len(seats[row])):
            if seats[row][col] == ".":
                row_new += "."
                # check_row += "."
            elif seats[row][col] == "L":
                chk = sit_check(seats, row, col)
                # check_row += str(chk)
                if chk > 0: row_new += "L"
                else:
                    row_new += "#"
                    changes += 1
            elif seats[row][col] == "#":
                chk = leave_check(seats, row, col)
                # check_row += str(chk)
                if chk < 4: row_new += "#"
                else:
                    row_new += "L"
                    changes += 1
        seats_new.append(row_new)
        # seat_checks.append(check_row)
    if changes:
        rounds += 1
        seats = seats_new
        # print()
        # for row in seats: print(row)
else:
    taken = 0
    for row in seats:
        taken += row.count("#")
        print(row)
print("\nRounds:", rounds, "\nNumber of seats taken:", taken)
