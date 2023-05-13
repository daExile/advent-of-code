file = open("17.txt", "r")
map_it = False
jets = file.read().strip()
cave = [ list("0000000") for _ in range(3) ]

#(y, x) for damn convenience
rocks = [[(0, 0), (0, 1), (0, 2), (0, 3)],
         [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
         [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
         [(0, 0), (1, 0), (2, 0), (3, 0)],
         [(0, 0), (0, 1), (1, 0), (1, 1)]]
n = 2022
jet = 0
cave_trim = True
cave_trim_stupid = False
cave_h = 0

for rocknum in range(n):
    stop = False
    r = None
    while not stop:
        if not r:
            r = rocks[rocknum % 5]
            ry = len(cave)
            rx = 2
            rh = max([i[0] for i in r]) + 1
            cave += [ list("0000000") for _ in range(rh) ]
        else:
            for j in r:
                if ry == 0 or cave[ry-1+j[0]][rx+j[1]] == "1":
                    stop = True
                    break
            if not stop: ry -= 1
            else:
                for j in r:
                    cave[ry+j[0]][rx+j[1]] = "1"
        #jets
        if not stop:
            shift = True
            if jet == len(jets): jet = 0
            dx = -1 if jets[jet] == "<" else 1
            jet += 1         
            for j in r:
                if rx+j[1]+dx < 0 or rx+j[1]+dx > 6 or cave[ry+j[0]][rx+j[1]+dx] == "1":
                    shift = False
                    break
            if shift: rx += dx
    if rocknum % 100000 == 0:
        print(rocknum)
        if cave_trim_stupid:
            cave_h += len(cave)-1000
            cave = cave[-1000:]        
        elif cave_trim:
            x = len(cave)-1
            while x >= 4:
                a = [int("".join(cave[x-i]), 2) for i in range(4)]
                b = (a[0] | a[1]) | (a[2] | a[3])
                if b == 127:
                    cave_h += x-3
                    cave = cave[x-3:]
                    break
                x -= 1
            
    stop = False            
    while not stop:
        if "1" not in cave[-1]: cave.pop(-1)
        else:
            cave += [ list("0000000") for _ in range(3) ]
            stop = True

cave_h += len(cave) - 3
if map_it:
    for i in range(len(cave)-3):
        print("".join(cave[len(cave)-4-i]))
print("P1:", cave_h)
