local function bitxor(a, b)
    local place_val, r = 1, 0
    
    repeat
        r, a, b, place_val = r + ((a % 2 + b % 2) % 2) * place_val, math.floor(a / 2), math.floor(b / 2), place_val * 2
    until a == 0 and b == 0
    
    return r
end

local function next_secret(secret) -- when you have LuaJIT power but not integer division / bitwise ops
    secret = bitxor(secret * 64, secret) % 16777216
    secret = bitxor(math.floor(secret / 32), secret) % 16777216
    secret = bitxor(secret * 2048, secret) % 16777216
    
    return secret
end

local secret_number_sum, buyer_id, sequence_log = 0, 0, {}
for line in io.lines("../__in/22.txt") do
    buyer_id = buyer_id + 1
    local n = tonumber(line); local price, diff, sequence = n % 10, 0, 0
    
    for i = 1, 2000 do
        n = next_secret(n)
        
        local price_next = n % 10; diff, price = price_next - price, price_next
        sequence = (sequence % 1000000) * 100 + 10 + diff
        
        if not sequence_log[sequence] then
            sequence_log[sequence] = {total = price, buyer_id = buyer_id}
        elseif sequence_log[sequence].buyer_id < buyer_id then
            sequence_log[sequence] = {total = sequence_log[sequence].total + price, buyer_id = buyer_id}
        end
    end
    secret_number_sum = secret_number_sum + n
end

print(string.format("Part 1: %.0f", secret_number_sum))

local best_total, best_seq = 0
for seq, data in pairs(sequence_log) do
    if seq > 1000000 and data.total > best_total then
        best_total = data.total
        
        t = {}; while seq > 0 do table.insert(t, 1, (seq % 100) - 10); seq = math.floor(seq / 100) end
        best_seq = table.concat(t, ",")
    end
end

print(string.format("Part 2: %d", best_total)) -- (sequence: %s)", best_total, best_seq))