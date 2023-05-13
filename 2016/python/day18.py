my_input = input("Puzzle input: ")
#my_input = ".^^.^.^^^^"  #test cases

m = []
rows = 400000

m.append("." + my_input + ".")
while len(m) < rows:
    row_n = ""
    for i in range(len(my_input)):
        a = m[-1][i:i+3]
        if a == "^.." or a == "^^." or a == ".^^" or a == "..^": row_n += "^"
        else: row_n += "."
    m.append("." + row_n + ".")

count = 0
for i in range(len(m)):
    count += m[i][1:-1].count(".")

print("Safe tiles:", count)
