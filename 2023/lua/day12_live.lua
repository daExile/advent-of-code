local cfg_mem = {}
local function configs(record, groups, l_max, r_st, g_st)
    g_st, r_st = g_st or 1, r_st or 1
    
    if not cfg_mem[l_max] then cfg_mem[l_max] = {} end  -- very clumsy timesaver
    if not cfg_mem[l_max][r_st] then cfg_mem[l_max][r_st] = {} end
    if cfg_mem[l_max][r_st][g_st] then return cfg_mem[l_max][r_st][g_st] end
    
    local count = 0
    for i = r_st, #record - l_max + 1 do
        local ok = true
        for j = r_st, i - 1 do if record[j] == "#" then ok = false end end
        for j = i, i + groups[g_st] - 1 do if record[j] == "." then ok = false end end

        if ok then
            if g_st == #groups then
                for j = i + groups[g_st], #record do if record[j] == "#" then ok = false end end
                if ok then count = count + 1 end
            else
                if record[i + groups[g_st]] == "#" then ok = false end
                if ok then count = count + configs(record, groups, l_max - groups[g_st] - 1, i + groups[g_st] + 1, g_st + 1) end
            end
        end
    end
    
    cfg_mem[l_max][r_st][g_st] = count; return count
end

local count1, count2 = 0, 0
for line in io.lines("../__in/12.txt") do
    local r_str, g_str = string.match(line, "([%.%?#]+) ([%d,]+)");
    
    local record, groups, l_max = {}, {}, 0
    for c in string.gmatch(r_str, ".") do table.insert(record, c) end
    for n in string.gmatch(g_str, "([%d]+)") do local x = tonumber(n); table.insert(groups, x); l_max = l_max + x end
    l_max = l_max + #groups - 1
    cfg_mem = {}; count1 = count1 + configs(record, groups, l_max)
    
    r_str = r_str.."?"..r_str.."?"..r_str.."?"..r_str.."?"..r_str
    g_str = g_str..","..g_str..","..g_str..","..g_str..","..g_str
    
    record, groups, l_max = {}, {}, 0
    for c in string.gmatch(r_str, ".") do table.insert(record, c) end
    for n in string.gmatch(g_str, "([%d]+)") do local x = tonumber(n); table.insert(groups, x); l_max = l_max + x end
    l_max = l_max + #groups - 1
    cfg_mem = {}; count2 = count2 + configs(record, groups, l_max)
end

print(string.format("Part 1: %d", count1))
print(string.format("Part 2: %.0f", count2))