file = open("02.txt", "r")

keypad = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7", "8", "9"]]

x = y = 1
code = ""
instructions = []
for line in file:
    instructions.append(line.strip())
file.close()

for i in instructions:
    for char in i:
        if char == "U": y = y - 1 if y > 0 else 0
        elif char == "D": y = y + 1 if y < 2 else 2
        elif char == "L": x = x - 1 if x > 0 else 0
        elif char == "R": x = x + 1 if x < 2 else 2
    code += keypad[y][x]

print("Code (puzzle part 1):", code)

keypad = [[" ", " ", "1", " ", " "],
          [" ", "2", "3", "4", " "],
          ["5", "6", "7", "8", "9"],
          [" ", "A", "B", "C", " "],
          [" ", " ", "D", " ", " "]]

x, y = 0, 2
code = ""

for i in instructions:
    for char in i:
        if char == "U": y = y if (y + x) == 2 or (y - x) == -2 else y - 1
        elif char == "D": y = y if (y + x) == 6 or (y - x) == 2 else y + 1
        elif char == "L": x = x if (y + x) == 2 or (y - x) == 2 else x - 1
        elif char == "R": x = x if (y + x) == 6 or (y - x) == -2 else x + 1
    code += keypad[y][x]

print("Code (puzzle part 2):", code)
