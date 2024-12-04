local function drop_nth(report, n)
    local t = {}
    for i, v in ipairs(report) do if i ~= n then table.insert(t, v) end end
    
    return t
end

local function sign(n) return (n > 0) and 1 or (n < 0) and -1 or 0 end

local function is_it_safe(report, dampen)
    local gaps = {}
    local signs = {[-1] = 0, [0] = 0, [1] = 0}
    
    for g = 1, #report - 1 do
        local delta = report[g + 1] - report[g]
        signs[sign(delta)] = signs[sign(delta)] + 1
        table.insert(gaps, {s = sign(delta), d = delta})
    end
    
    local trend = (signs[1] > signs[-1]) and 1 or -1
    
    local bad_gaps = {}
    for g = 1, #report - 1 do if gaps[g].s ~= trend or math.abs(gaps[g].d) > 3 then table.insert(bad_gaps, g) end end
    
    if #bad_gaps == 0 then return true
    elseif dampen and #bad_gaps == 1 then
        return is_it_safe(drop_nth(report, bad_gaps[1])) or is_it_safe(drop_nth(report, bad_gaps[1] + 1))
    elseif dampen and #bad_gaps == 2 and bad_gaps[2] - bad_gaps[1] == 1 then
        return is_it_safe(drop_nth(report, bad_gaps[2]))
    end
    
    return false
end

local count1, count2 = 0, 0        
for line in io.lines("../__in/02.txt") do
    local report = {}
    for n in line:gmatch("%d+") do table.insert(report, tonumber(n)) end
    
    count1, count2 = count1 + (is_it_safe(report) and 1 or 0), count2 + (is_it_safe(report, true) and 1 or 0)   
end

print(string.format("Part 1: %d", count1))
print(string.format("Part 2: %d", count2))