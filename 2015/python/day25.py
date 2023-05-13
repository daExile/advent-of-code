print("Puzzle input")
row = int(input("Row: "))
col = int(input("Column: "))

code = 20151125
n = 1

diag = row + col - 1
n_we_are_looking_for = int((diag * (diag - 1))/2) + col

while n < n_we_are_looking_for:
    code = (code * 252533) % 33554393
    n += 1

print("Code we are looking for:", code)
