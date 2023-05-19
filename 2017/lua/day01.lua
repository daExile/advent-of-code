require("stuff")

input = stuff.str2alnumchartable(io.open("01.txt", "r"):read())
len = #input

checksum1, checksum2 = 0, 0

for i = 1, len do
    str_a = input[i]
    str_check1 = input[i % len + 1]
    str_check2 = input[(len / 2 + i - 1) % len + 1]
    
    if str_a == str_check1 then checksum1 = checksum1 + str_a end
    if str_a == str_check2 then checksum2 = checksum2 + str_a end
end

print(string.format("Part 1: %d", checksum1))
print(string.format("Part 2: %d", checksum2))