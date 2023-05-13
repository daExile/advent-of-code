file = open("01.txt", "r")

s = file.read()
file.close()

a = s.count("(")
b = s.count(")")
print("Part 1 answer:", a - b)

floor, step = 0, 0
for char in s:
    step += 1
    floor = floor + 1 if char == "(" else floor - 1

    if floor == -1: break
print("Part 2 answer:", step)
