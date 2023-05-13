file = open("17.txt", "r")
import hashlib
jets = file.read().strip()
trim = False
tf = 60
cave = [0, 0, 0]

#(y, x) for damn convenience
rocks = [[[15], 3],
         [[2, 7, 2], 2],
         [[7, 1, 1], 2],
         [[1, 1, 1, 1], 0],
         [[3, 3], 1]]
n = 1000000000000
jet = 0
cave_h = 0
log = {}
def map_it():
    for i in range(len(cave)-1, -1, -1):
        print("{:07b}".format(cave[i]))
    print("\n")

rocknum = 0
hashmatch = False
while rocknum < n:
    if not hashmatch:
        if len(cave) > 100:
            cx = "".join(["{:02x}".format(cave[i]) for i in range(-100, 0)])
            ch = hashlib.md5(cx.encode()).hexdigest()
            log_entry = (ch, rocknum % 5, jet)
            if log_entry not in log: log[log_entry] = (rocknum, len(cave))
            else:
                drocknum = rocknum - log[log_entry][0]
                dcave = len(cave) - log[log_entry][1]
                c, rem = divmod(n-rocknum, drocknum)
                print(drocknum, dcave, c, rem)
                rocknum = rocknum + c*drocknum
                print(rocknum)
                cave_h += c*dcave

                hashmatch = True
    #if (rocknum % 5, jet) in log: print("yay", rocknum)
    #else: log.append((rocknum % 5, jet))

    stop = False
    r = None
    while not stop:
        if not r:
            r = rocks[rocknum % 5]
            ry = len(cave)
            rx = 2
            rh = len(r[0]) + 1
            cave += [0] * rh            
        else:
            for i, row in enumerate(r[0]):
                if ry == 0 or cave[ry-1+i] & (row << (6-rx-r[1])) != 0:
                    stop = True
                    break
            if not stop: ry -= 1
            else:
                for i, row in enumerate(r[0]):
                    cave[ry+i] = cave[ry+i] + (row << (6-rx-r[1]))
        #jets
        if not stop:
            shift = True
            if jet == len(jets): jet = 0
            dx = -1 if jets[jet] == "<" else 1
            jet += 1
            for i, row in enumerate(r[0]):
                if rx+dx < 0 or 6-rx-r[1]-dx < 0 or cave[ry+i] & (row << (6-rx-r[1]-dx)) != 0:
                    shift = False
                    break
            if shift:
                rx += dx

    #map_it()     
    stop = False            
    while not stop:
        if cave[-1] == 0: cave.pop(-1)
        else: stop = True
    #trim
    #if len(cave) > 4:
    #    if (cave[-1] & cave[-2]) & (cave[-3] & cave[-4]) == 127:
    #        cave_h += len(cave)-4
    #        cave = cave[-4:]
    
    #stupid trim
    if trim:
        if len(cave) > tf:
            cave_h += len(cave) - tf
            cave = cave[-tf:]
        
    cave += [0] * 3
    rocknum += 1

cave_h += len(cave) - 3
print("P2:", cave_h)
