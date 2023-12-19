local function get_digits(str)
    local t = {}
    for item in string.gmatch(str, "%d") do table.insert(t, tonumber(item)) end
    return t end

-- find and replace in a way that won't break overlapped "digits"
local digits = {{"one", "o1e"}, {"two", "t2o"}, {"three", "t3e"}, {"four", "4"}, {"five", "5e"}, {"six", "6"}, {"seven", "7n"}, {"eight", "e8t"}, {"nine", "n9e"}}

local checksum1, checksum2 = 0, 0
for line in io.lines("../__in/01.txt") do
    local nums = get_digits(line); checksum1 = checksum1 + 10 * nums[1] + nums[#nums]
    
    for _, d in pairs(digits) do line = string.gsub(line, d[1], d[2]) end
    nums = get_digits(line); checksum2 = checksum2 + 10 * nums[1] + nums[#nums]
end

print(string.format("Part 1: %d", checksum1))
print(string.format("Part 2: %d", checksum2))