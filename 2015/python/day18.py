file = open("18.txt", "r")
#file = [".#.#.#",
#        "...##.",
#        "#....#",
#        "..#...",
#        "#.#..#",
#        "####.."]

board = []
bins = str.maketrans(".#", "01")
for line in file:
    board.append([int(i) for i in list(line.strip().translate(bins))])
file.close()

turns = 100
corners_stuck = True
if corners_stuck:
    board[0][0] = 1
    board[0][99] = 1
    board[99][0] = 1
    board[99][99] = 1

for t in range(turns):
    board_next = []
    for i, row in enumerate(board):
        y1 = i - 1 if i > 0 else 0
        y2 = i + 1 if i < len(board) - 1 else len(board) - 1
        row_next = []
        for j, light in enumerate(row):
            if corners_stuck and (i, j) in [(0, 0), (0, 99), (99, 0), (99, 99)]:
                row_next.append(1)
            else:
                a = 0
                x1 = j - 1 if j > 0 else 0
                x2 = j + 1 if j < len(row) - 1 else len(row) - 1
                for y in range(y1, y2+1):
                    for x in range(x1, x2+1):
                        if (y, x) != (i, j): a += board[y][x]
                if (board[i][j] and 2 <= a <= 3) or (not board[i][j] and a == 3):
                    row_next.append(1)
                else: row_next.append(0)
        board_next.append(row_next)
    board = board_next

count = 0
for row in board: count += sum(row)

print("Part {} answer: {}".format(2 if corners_stuck else 1, count))
