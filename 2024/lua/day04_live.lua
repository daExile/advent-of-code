local word_search, count1, count2 = {}, 0, 0
local deltas = {{r = 0, c = 1}, {r = 1, c = 1}, {r = 1, c = 0}, {r = 1, c = -1}}

local function find_xmas(board, r, c, d)
    if board[r + 3 * d.r] and board[r + 3 * d.r][c + 3 * d.c] then
        local word = ""; for i = 0, 3 do word = word .. board[r + i * d.r][c + i * d.c] end
        
        return word == "XMAS" or word == "SAMX"
    end
    
    return false
end

local function find_x_mas(board, r, c)
    if r > 1 and r < #board and c > 1 and c < #board[r] then
        local w1 = board[r - 1][c - 1] .. board[r][c] .. board[r + 1][c + 1]
        local w2 = board[r + 1][c - 1] .. board[r][c] .. board[r - 1][c + 1]
        
        return (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM")
    end
    
    return false
end

for line in io.lines("../__in/04.txt") do
    local row = {}; for c in line:gmatch(".") do table.insert(row, c) end
    table.insert(word_search, row)
end

for r = 1, #word_search do
    for c = 1, #word_search[r] do
        if word_search[r][c] == "S" or word_search[r][c] == "X" then
            for _, d in ipairs(deltas) do count1 = count1 + (find_xmas(word_search, r, c, d) and 1 or 0) end
        end
        
        if word_search[r][c] == "A" then count2 = count2 + (find_x_mas(word_search, r, c) and 1 or 0) end
    end
end

print(string.format("Part 1: %d", count1))
print(string.format("Part 2: %d", count2))