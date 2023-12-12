local points, cards, card_count, id_max = 0, 0, {}

for line in io.lines("../__in/04.txt") do
    local id, win, have = string.match(line, "Card[%s]+([%d]+): ([%d%s]+) | ([%d%s]+)")
    local t_win, count = {}, 0; id = tonumber(id)

    card_count[id] = (card_count[id] or 0) + 1;     
    for n in string.gmatch(win, "([%d]+)") do t_win[n] = true end
    for n in string.gmatch(have, "([%d]+)") do if t_win[n] then count = count + 1 end end
    
    if count > 0 then points = points + math.pow(2, count - 1) end
    for i = 1, count do card_count[id + i] = (card_count[id + i] or 0) + card_count[id] end
    id_max = id
end

print(string.format("Part 1: %d", points))

for i = 1, id_max do cards = cards + card_count[i] end
print(string.format("Part 2: %d", cards))