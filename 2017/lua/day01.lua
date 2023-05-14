file = io.open("01.txt", "r")

--input = "123425"
input = file:read()

len = #input

function strindex2num(s, i) return string.sub(s, i, i) end

checksum1, checksum2 = 0, 0
for i = 1, len do
    str_a = strindex2num(input, i)
    str_check1 = strindex2num(input, (i % len + 1))
    str_check2 = strindex2num(input, (len / 2 + i - 1) % len + 1)
    --print(str_a, str_check1, str_check2)
    if str_a == str_check1 then checksum1 = checksum1 + str_a end
    if str_a == str_check2 then checksum2 = checksum2 + str_a end
end

print(string.format("Part 1: %d", checksum1))
print(string.format("Part 2: %d", checksum2))
io.close(file)