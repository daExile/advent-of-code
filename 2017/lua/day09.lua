local stuff = require("stuff")

local input_with_cancels = string.gsub((io.open("../__in/09.txt", "r"):read()), "!.", "")
local input_no_garbo = stuff.str2anychartable(string.gsub(input_with_cancels, "<[^>]*>", "<>"))

local tier, score = 0, 0
for _, char in ipairs(input_no_garbo) do
    if char == "{" then tier = tier + 1; score = score + tier elseif char == "}" then tier = tier - 1 end end

print(string.format("Part 1: %d", score))
print(string.format("Part 2: %d", #input_with_cancels - #input_no_garbo))