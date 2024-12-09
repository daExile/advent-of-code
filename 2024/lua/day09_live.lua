local p1_block_map = {}
local p2_file_map, p2_empty_map = {}, {{}, {}, {}, {}, {}, {}, {}, {}, {}}

local ptr, file_id = 0
for file, empty in io.open("../__in/09.txt"):read():gmatch("(%d)(%d?)") do
    file_id = (file_id and file_id + 1 or 0)
    file, empty = tonumber(file), tonumber(empty)
    
    -- primitive block mapping for part 1
    for i = 1, file do table.insert(p1_block_map, file_id) end    
    for i = 1, (empty or 0) do table.insert(p1_block_map, -1) end
    
    -- i guess i need something fancier for part 2
    p2_file_map[file_id] = {s = ptr, e = ptr + file - 1}; ptr = ptr + file
    
    if empty and empty > 0 then
        if not p2_empty_map[empty] then p2_empty_map[empty] = {} end
        table.insert(p2_empty_map[empty], ptr); ptr = ptr + empty
    end
end

-- part 1: remapping / calculating checksum
local checksum1, ptrL, ptrR = 0, 1, #p1_block_map
while ptrL <= ptrR do
    if p1_block_map[ptrL] < 0 then
        p1_block_map[ptrL] = table.remove(p1_block_map); ptrR = ptrR - 1
        while p1_block_map[ptrR] < 0 do table.remove(p1_block_map); ptrR = ptrR - 1 end
    end
    
    checksum1, ptrL = checksum1 + p1_block_map[ptrL] * (ptrL - 1), ptrL + 1
end

-- part 2: clumsy convoluted mess
local checksum2 = 0
for i = file_id, 0, -1 do
    local len = p2_file_map[i].e - p2_file_map[i].s + 1
    
    -- look for leftmost gap to fit this file
    local gap, gap_size
    for l = len, 9 do
        if #p2_empty_map[l] > 0 then
            if not gap or gap > p2_empty_map[l][1] then gap, gap_size = p2_empty_map[l][1], l end
        end
    end
    
    -- move the file if a suitable place was found, care not about empty space left behind due to file processing order
    if gap and p2_file_map[i].s > gap then
        p2_file_map[i] = {s = gap, e = gap + len - 1}
        
        table.remove(p2_empty_map[gap_size], 1)         -- delete gap entry
        
        if gap_size > len then                          -- add remaining gap entry, if there is a leftover
            gap, gap_size = gap + len, gap_size - len
            local j = 1; while p2_empty_map[gap_size][j] and gap > p2_empty_map[gap_size][j] do j = j + 1 end
            table.insert(p2_empty_map[gap_size], j, gap)
        end
    end
    
    -- add the file checksum
    checksum2 = checksum2 + (p2_file_map[i].s * len + (len * (len - 1)) / 2) * i
end

print(string.format("Part 1: %.0f", checksum1))
print(string.format("Part 2: %.0f", checksum2))