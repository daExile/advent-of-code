local input = io.open("../__in/15.txt", "r"):read()

local sum1, sum2, lenses = 0, 0, {}
for str in string.gmatch(input, "([^,]+)") do
    local c_val = 0
    for char in string.gmatch(str, ".") do c_val = (c_val + string.byte(char)) * 17 % 256 end
    sum1 = sum1 + c_val
    
    local lens_id, op, focal_len = string.match(str, "([A-Za-z]+)([-=])(.*)")
    c_val = 0; for char in string.gmatch(lens_id, "[A-Za-z]") do c_val = (c_val + string.byte(char)) * 17 % 256 end
    
    if not lenses[c_val] then if op == "=" then lenses[c_val] = {{lens_id, focal_len}} end
    else
        if op == "-" then
            for i, lens in ipairs(lenses[c_val]) do if lens[1] == lens_id then table.remove(lenses[c_val], i); break end end
        elseif op == "=" then
            local lens_found = false
            for i, lens in ipairs(lenses[c_val]) do
                if lens[1] == lens_id then lens[2] = focal_len; lens_found = true; break end end
            if not lens_found then table.insert(lenses[c_val], {lens_id, focal_len}) end
        end
    end
end

print(string.format("Part 1: %d", sum1))

for box_id = 0, 256 do
    if lenses[box_id] then
        for n, lens in ipairs(lenses[box_id]) do
            sum2 = sum2 + (box_id + 1) * n * lens[2] end end end
print(string.format("Part 2: %d", sum2))