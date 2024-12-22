local count1, count2 = 0, 0
local patterns, design_memo, input = {}, {}, io.lines("../__in/19.txt")

local p_str = input(); for p in p_str:gmatch("(%w+)") do table.insert(patterns, p) end; input()

local function design_check(design_str, patterns)
    if design_memo[design_str] then return design_memo[design_str] end
    
    local count, str_len = 0, #design_str
    
    for _, p in ipairs(patterns) do
        local p_len = #p
        if p_len <= str_len then
            local l, r = design_str:sub(1, p_len), design_str:sub(p_len + 1)
            if l == p then count = count + (#r > 0 and design_check(r, patterns) or 1) end
        end
    end
    
    design_memo[design_str] = count; return count
end

for design in input do
    local n = design_check(design, patterns); count1, count2 = count1 + (n > 0 and 1 or 0), count2 + n   
end

print(string.format("Part 1: %d", count1))
print(string.format("Part 2: %.0f", count2))