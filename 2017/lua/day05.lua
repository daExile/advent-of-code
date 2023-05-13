function jumparound(t, part2)
  local jumps, index = 0, 1
  
  while true do
    if not t[index] then break end
  
    local newindex = index + t[index]
  
    if part2 then if t[index] >= 3 then t[index] = t[index] - 1 else t[index] = t[index] + 1 end
    else t[index] = t[index] + 1 end
  
    jumps = jumps + 1
    index = newindex
  end
  return jumps end

run1, run2 = {}, {}
for v in io.lines("05.txt") do
  table.insert(run1, tonumber(v))
  table.insert(run2, tonumber(v))
end

print(string.format("Part 1: %d", jumparound(run1, false)))
print(string.format("Part 2: %d", jumparound(run2, true)))