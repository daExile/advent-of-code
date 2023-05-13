require("stuff")

function findanddivide(t)
  for i = 1, #t - 1 do
    for j = i + 1, #t do
      if t[i] % t[j] == 0 then return t[i] / t[j] end
      if t[j] % t[i] == 0 then return t[j] / t[i] end
    end
  end
end

checksum1, checksum2 = 0, 0
for line in io.lines("02.txt") do
  nums = stuff.str2numtable(line)
  limits = stuff.tableminmax(nums)
  checksum1 = checksum1 + limits[2] - limits[1]
  checksum2 = checksum2 + findanddivide(nums)
end

print(string.format("Part 1: %d", checksum1))
print(string.format("Part 2: %d", checksum2))