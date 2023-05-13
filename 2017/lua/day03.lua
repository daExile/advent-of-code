function turnleft(t) return {t[2] * -1, t[1] * 1} end

function get3x3sum(node)
  local sum = 0
  for i = node[1] - 1, node[1] + 1 do
    for j = node[2] - 1, node[2] + 1 do
      if grid[i] then
        if grid[i][j] then sum = sum + grid[i][j] end
      end
    end
  end
  return sum end

function addnode(node, value)
  if not grid[node[1]] then grid[node[1]] = {} end
  grid[node[1]][node[2]] = value end
  
function nextnode(node, dir)
  local newnode = {node[1] + dir[1], node[2] + dir[2]}
  local newdir = turnleft(dir)
  if not grid[newnode[1] + newdir[1]] or not grid[newnode[1] + newdir[1]][newnode[2] + newdir[2]] then return newnode, newdir
  else return newnode, dir end
end

print("Puzzle input is...")
input = io.read("*n")

-- part 1, instead of fancy math let's generate the grid for practice
grid = {}
node, dir = {0, 0}, {1, 0}
value = 1

repeat
  addnode(node, value)
  node, dir = nextnode(node, dir)
  value = value + 1
until value == input

print(string.format("Part 1: %d", math.abs(node[1]) + math.abs(node[2])))

-- part 2
grid = {}
node, dir = {0, 0}, {1, 0}
value = 1

repeat
  addnode(node, value)
  node, dir = nextnode(node, dir)
  value = get3x3sum(node)
until value > input

print(string.format("Part 2: %d", value))