require("stuff")

function strsort(str)
  local t = stuff.str2chartable(str)
  table.sort(t)
  return table.concat(t) end

c_all, c_valid1, c_valid2 = 0, 0, 0
for line in io.lines("04.txt") do
  local t1, t2 = {}, {}
  c_all = c_all + 1
  words = stuff.str2strtable(line)
  
  for i = 1, #words do
    t1[words[i]] = true
    t2[strsort(words[i])] = true end
    
  if stuff.tablesize(t1) == #words then c_valid1 = c_valid1 + 1 end
  if stuff.tablesize(t2) == #words then c_valid2 = c_valid2 + 1 end
end

--print("Total passphrases:", c_all)
print(string.format("Part 1: %d", c_valid1))
print(string.format("Part 2: %d", c_valid2))