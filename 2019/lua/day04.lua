local n_start, n_end = string.match(io.open("../__in/04.txt", "r"):read(), "(%d+)%-(%d+)"); io.close()

local count1, count2 = 0, 0

local function checknumber(n)
    local digits, p1check, a, b = {}, 0, 9
    repeat
        b = n % 10
        if b > a then return 0, 0 end
        
        n, a, digits[b] = math.floor(n / 10), b, (digits[b] or 0) + 1
    until n == 0
    
    for i = 0, 9 do
        if digits[i] then
            if digits[i] == 2 then return 1, 1
            elseif digits[i] > 2 then p1check = 1 end end end
            
    return p1check, 0 end

for n = tonumber(n_start), tonumber(n_end) do
    local check1, check2 = checknumber(n)
    count1, count2 = count1 + check1, count2 + check2 end

print(string.format("Part 1: %d", count1))
print(string.format("Part 2: %d", count2))