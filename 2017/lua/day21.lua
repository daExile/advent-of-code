local stuff = require("stuff")

local function rotate(t)
    local t_new, size = {}, #t
    for row = 1, size do
        t_new[row] = {}
        for col = 1, size do t_new[row][col] = t[size - col + 1][row] end end
    return t_new end

local function flip(t)
    local t_new, size = {}, #t
    for row = 1, size do t_new[row] = t[size - row + 1] end
    return t_new end
    
local function iterate(image, rulebook, iterations)
    for iter = 1, iterations do
        local tiles, step
        if #image % 2 == 0 then step = 2 else step = 3 end
        tiles = #image / step
    
        local image_new = {}
        for row = 0, tiles - 1 do
            for col = 0, tiles - 1 do
                local tmp = ""
                for i = 1, step do tmp = tmp..string.sub(image[row * step + i], col * step + 1, col * step + step) end
                
                local k, n = row * (step + 1), tonumber(tmp, 2) + 1
                for i = 1, step + 1 do
                    if not image_new[k + i] then image_new[k + i] = rulebook[step][n][i]
                    else image_new[k + i] = image_new[k + i]..rulebook[step][n][i] end
                end
            end
        end
        image = image_new
    end
    return image end
    
local function subst(char) if char == "#" then return "1" end return "0" end

local rulebook, image = { {}, {}, {} }, {"010", "001", "111"} -- standard input {".#.", "..#", "###"} turned binary
for line in io.lines("21.txt") do
    local str_in, str_out = string.match(string.gsub(line, "[.#]", subst), "([01/]+) => ([01/]+)")
    local out = {}; for item in string.gmatch(str_out, "([01]+)") do table.insert(out, item) end
    local t = {}
    for chunk in string.gmatch(str_in, "([01]+)") do table.insert(t, stuff.str2anychartable(chunk)) end
    
    for i = 1, 2 do
        for j = 1, 4 do
            local tmp = {}
            for k = 1, #t do table.insert(tmp, table.concat(t[k])) end
            str_in = table.concat(tmp)
            
            if #str_in == 4 then rulebook[2][tonumber(str_in, 2) + 1] = out
            else rulebook[3][tonumber(str_in, 2) + 1] = out end
            
            t = rotate(t)
        end
        t = flip(t)
    end
end

local image, count = iterate(image, rulebook, 5), 0
for row = 1, #image do count = count + #string.gsub(image[row], "0", "") end
print(string.format("Part 1: %d", count))

image, count = iterate(image, rulebook, 13), 0
for row = 1, #image do count = count + #string.gsub(image[row], "0", "") end
print(string.format("Part 2: %d", count))