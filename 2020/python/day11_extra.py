def sit_check(seats, row, col):
    occ = 0
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

def leave_check(seats, row, col):
    occ = 0
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
                if chk < 5: row_new += "#"
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
