input = tonumber(io.open("17.txt", "r"):read())

buffer, n, pos = {[0] = 0}, 0, 0

while n < 2017 do
    n = n + 1
    for i = 1, input do pos = buffer[pos] end
    
    buffer[n], buffer[pos] = buffer[pos], n; pos = buffer[pos]
end

current, pos = 0, 0
while current ~= 2017 do current, pos = buffer[current], pos + 1 end

while n < 50000000 do
    n = n + 1
    pos = (pos + input) % n + 1
    if pos == 1 then target = n end
end

print(string.format("Part 1: %d", buffer[2017]))
print(string.format("Part 2: %d", target))