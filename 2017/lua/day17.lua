input = tonumber(io.open("17.txt", "r"):read())

buffer, pos = {[0] = 0}, 0

for n = 1, 2017 do
    for i = 1, input do pos = buffer[pos] end
    
    buffer[n], buffer[pos] = buffer[pos], n; pos = buffer[pos] end

current, pos = 0, 0 -- looking up for "index" of 2017 in resulting table to...
while current ~= 2017 do current, pos = buffer[current], pos + 1 end

for n = 2018, 50000000 do -- ...continue from where part 1 stopped for no reason :)
    pos = (pos + input) % n + 1
    if pos == 1 then target = n end end

print(string.format("Part 1: %d", buffer[2017]))
print(string.format("Part 2: %d", target))