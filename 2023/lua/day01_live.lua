local function get_digits(str)
    local t = {}
    for item in string.gmatch(str, "%d") do table.insert(t, tonumber(item)) end
    return t end

local list = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
local checksum1, checksum2 = 0, 0
for line in io.lines("../__in/01.txt") do
    local nums = get_digits(line)
    checksum1 = checksum1 + 10 * nums[1] + nums[#nums]
    
    repeat
        local match, imatch
        for i, p in ipairs(list) do
            m = string.find(line, p)
            if m and (not match or m < match) then match = m; imatch = i end
        end
        
        if match then line = string.gsub(line, list[imatch], string.format("%d%s", imatch, string.sub(list[imatch], 2)), 1) end
    until not match
    
    nums = get_digits(line)
    checksum2 = checksum2 + 10 * nums[1] + nums[#nums]
end

print(string.format("Part 1: %d", checksum1))
print(string.format("Part 2: %d", checksum2))