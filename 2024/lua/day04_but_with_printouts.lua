local count1, count2 = 0, 0
local word_search, deltas = {}, {{r = 0, c = 1}, {r = 1, c = 1}, {r = 1, c = 0}, {r = 1, c = -1}}

-- i mapped the tiles making up XMASes as i thought we'll have to count them in part 2
-- turns out, mapping them was only good for printouts, so, here are some printouts!
local result_xmas, result_x_mas = {}, {}

local function find_xmas(board, result, r, c, d)
    if board[r + 3 * d.r] and board[r + 3 * d.r][c + 3 * d.c] then
        local word = ""; for i = 0, 3 do word = word .. board[r + i * d.r][c + i * d.c] end
        
        if word == "XMAS" or word == "SAMX" then
            for i = 0, 3 do result[r + i * d.r][c + i * d.c] = board[r + i * d.r][c + i * d.c] end
            return true
        end
    end
    
    return false
end

local function find_x_mas(board, result, r, c)
    if r > 1 and r < #board and c > 1 and c < #board[r] then
        local w1 = board[r - 1][c - 1] .. board[r][c] .. board[r + 1][c + 1]
        local w2 = board[r + 1][c - 1] .. board[r][c] .. board[r - 1][c + 1]
        
        if (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM") then
            result[r][c] = board[r][c]
            local dr, dc = -1, -1; for i = 1, 4 do result[r + dr][c + dc] = board[r + dr][c + dc]; dr, dc = -dc, dr end
            return true
        end
    end
    
    return false
end

for line in io.lines("../__in/04.txt") do
    local row_ws, row_xmas, row_x_mas = {}, {}, {}
    for c in line:gmatch(".") do table.insert(row_ws, c); table.insert(row_xmas, "."); table.insert(row_x_mas, ".") end
    
    table.insert(word_search, row_ws); table.insert(result_xmas, row_xmas); table.insert(result_x_mas, row_x_mas)
end

for r = 1, #word_search do
    for c = 1, #word_search[r] do
        if word_search[r][c] == "S" or word_search[r][c] == "X" then
            for _, d in ipairs(deltas) do
                count1 = count1 + (find_xmas(word_search, result_xmas, r, c, d) and 1 or 0)
            end
        end
        
        if word_search[r][c] == "A" then count2 = count2 + (find_x_mas(word_search, result_x_mas, r, c) and 1 or 0) end
    end
end

print(string.format("Part 1: %d", count1)); for r = 1, #result_xmas do print(table.concat(result_xmas[r])) end
print(string.format("\nPart 2: %d", count2)); for r = 1, #result_xmas do print(table.concat(result_x_mas[r])) end