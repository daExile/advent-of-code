function new(x, n) x = (x * n) % 2147483647; return x end

function new_mult(x, m, n) repeat x = new(x, n) until x % m == 0; return x end

starters = {}
for line in io.lines("15.txt") do table.insert(starters, tonumber(string.match(line, "(%d+)"))) end

count1, count2 = 0, 0

a, b = starters[1], starters[2]
for i = 1, 40000000 do
    a, b = new(a, 16807), new(b, 48271)
    if (a - b) % 65536 == 0 then count1 = count1 + 1 end
end
print(string.format("Part 1: %d", count1))

a, b = starters[1], starters[2]
for i = 1, 5000000 do
    a, b = new_mult(a, 4, 16807), new_mult(b, 8, 48271) --new_a4(), new_b8()
    if (a - b) % 65536 == 0 then count2 = count2 + 1 end end
print(string.format("Part 2: %d", count2))