local input = io.open("../__in/13.txt", "r"):read("*a")
local claw_machine_pattern = ".-A: X%+(%d+), Y%+(%d+).-B: X%+(%d+), Y%+(%d+).-Prize: X=(%d+), Y=(%d+)"

local function tokens_to_win(aX, aY, bX, bY, X, Y)
    local a_num, a_den = bY * X - bX * Y, bY * aX - bX * aY
    
    if a_num % a_den == 0 then
        local a = a_num / a_den; local b_num = Y - aY * a
        if b_num % bY == 0 then return 3 * a + b_num / bY end
    end
    
    return 0
end

local tokens1, tokens2 = 0, 0
for aX, aY, bX, bY, X, Y in input.gmatch(input, claw_machine_pattern) do
    tokens1 = tokens1 + tokens_to_win(aX, aY, bX, bY, X, Y)
    tokens2 = tokens2 + tokens_to_win(aX, aY, bX, bY, 10000000000000 + X, 10000000000000 + Y)
end

print(string.format("Part 1: %d", tokens1))
print(string.format("Part 2: %.0f", tokens2))