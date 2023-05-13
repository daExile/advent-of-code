file = open("14.txt", "r")

rock = []
xmin = xmax = 500
ymax = 0
floor = True
save_it = False

def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    return 0

for line in file:
    s = line.strip().split(" -> ")
    sn = []
    for i in s:
        x, y = [int(x) for x in i.split(",")]
        if xmin > x: xmin = x
        if xmax < x: xmax = x
        if ymax < y: ymax = y
        sn.append((x, y))
    rock.append(sn)
file.close()
#i'll just hardcode it to width of 401 for now
chart =  [ [ "." for _ in range(401) ] for _ in range(0, ymax+2) ]
if floor:
    chart.append( [ "#" for _ in range(401) ] )

for r in rock:
    for i in range(len(r)-1):
        delx = r[i+1][0] - r[i][0]
        dely = r[i+1][1] - r[i][1]
        dx = sign(delx)
        dy = sign(dely)
        for j in range(max(delx * dx, dely * dy) + 1):
            #print(r[i][0]+dx*j, r[i][1]+dy*j)
            chart[r[i][1]+dy*j][r[i][0]+dx*j-300] = "#"
    
#TIME TO THROW SAND IN
#in a very lazy simulation
stahp = False
sand = 0
while not stahp:
    x = 200
    y = 0
    while True:
        if x == 0 or x == len(chart[0])-1 or y == len(chart)-1:
            stahp = True
            chart[y][x] = "X"
            break        
        if chart[y+1][x] == ".": y += 1
        elif chart[y+1][x-1] == ".":
            y += 1
            x -= 1
        elif chart[y+1][x+1] == ".":
            y += 1
            x += 1
        else:
            chart[y][x] = "O"
            sand += 1
            if x == 200 and y == 0: stahp = True
            break

if save_it:
    file = open("14_chart.txt", "w")
    for row in chart:
        file.write("".join(row) + "\n")
    file.close()
else:
    for row in chart:
        print("".join(row[175:226]))

print("Final sand count:", sand)
