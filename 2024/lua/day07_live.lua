local total1, total2 = 0, 0

local function calibrate(target, numbers, result, i)
    i = i or 1; if not numbers[i] or (result and result > target) then return result == target end
    
    return
        calibrate(target, numbers, (result or 0) + numbers[i], i + 1)
        or (result and calibrate(target, numbers, result * numbers[i], i + 1))
end

local function calibrate_with_concat(target, numbers, result, i)
    i = i or 1; if not numbers[i] or (result and result > target) then return result == target end
    
    local k = (numbers[i] < 10 and 10) or (numbers[i] < 100 and 100) or 1000
    return
        calibrate_with_concat(target, numbers, (result or 0) + numbers[i], i + 1)
        or (result and calibrate_with_concat(target, numbers, result * numbers[i], i + 1))
        or (result and calibrate_with_concat(target, numbers, k * result + numbers[i], i + 1))
end

for line in io.lines("../__in/07.txt") do
    local left, right = line:match("(%d+):%s([%d%s]+)")
    local target, numbers = tonumber(left), {}
    for n in right:gmatch("%d+") do table.insert(numbers, tonumber(n)) end
    
    c1 = calibrate(target, numbers); c2 = c1 or calibrate_with_concat(target, numbers)
    total1, total2 = total1 + (c1 and target or 0), total2 + (c2 and target or 0)
end

print(string.format("Part 1: %.0f", total1))
print(string.format("Part 2: %.0f", total2))