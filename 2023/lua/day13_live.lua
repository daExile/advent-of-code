local input, n, score1, score2 = {}, 1, 0, 0
for line in io.lines("../__in/13.txt") do table.insert(input, line) end

while input[n] do
    local frag = {}
    while input[n] and input[n] ~= "" do
        local line = {}
        for tile in string.gmatch(input[n], ".") do table.insert(line, tile) end        
        table.insert(frag, line); n = n + 1 end
        
        n = n + 1
    
    for i = 1, #frag - 1 do -- terrible nested loop to check for clear / one-off reflections, horizontal part
        local ref_score = 0
        for j = i, 1, -1 do
            if frag[2 * i - j + 1] then 
                for k = 1, #frag[1] do
                    if frag[j][k] ~= frag[2 * i - j + 1][k] then ref_score = ref_score + 1 end end end end
        
        if ref_score == 0 then score1 = score1 + 100 * i end
        if ref_score == 1 then score2 = score2 + 100 * i end
    end
    
    for i = 1, #frag[1] - 1 do  -- ...and vertical part
        local ref_score = 0
        for j = i, 1, -1 do
            if frag[1][2 * i - j + 1] then 
                for k = 1, #frag do
                    if frag[k][j] ~= frag[k][2 * i - j + 1] then ref_score = ref_score + 1 end end end end
        
        if ref_score == 0 then score1 = score1 + i end
        if ref_score == 1 then score2 = score2 + i end
    end
end

print(string.format("Part 1: %d", score1))
print(string.format("Part 2: %d", score2))