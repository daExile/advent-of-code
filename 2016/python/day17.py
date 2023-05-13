my_input = input("Puzzle input: ")
#my_input = "kglvqrro"  #test case

from hashlib import md5
import re

def get_doors(path, c):
    x, y = c
    h = [i.start() for i in re.finditer(r"[b-f]", md5(path.encode()).hexdigest()[:4])]
    doors = []
    for i, d in enumerate(["U", "D", "L", "R"]):
        if i in h:
            if i == 0 and y > 0: doors.append(d)
            elif i == 1 and y < 3: doors.append(d)
            elif i == 2 and x > 0: doors.append(d)
            elif i == 3 and x < 3: doors.append(d)
    return doors

def nav(path, c):
    if c == (3, 3):
        paths_found.append(path)
    else:
        d = get_doors(my_input + path, c)
        if d:
            for door in d:
                if door == "U": c_new = (c[0], c[1] - 1)
                elif door == "D": c_new = (c[0], c[1] + 1)
                elif door == "L": c_new = (c[0] - 1, c[1])
                elif door == "R": c_new = (c[0] + 1, c[1])
                path_new = path + door
                nav(path_new, c_new)

path = ""
paths_found = []
c = (0, 0)

nav(path, c)
paths_found.sort(key = lambda x: len(x))
print("Total paths to vault found: {}".format(len(paths_found)))
print("Shortest path: {} (with a length of {})".format(paths_found[0], len(paths_found[0])))
print("Longest path: {} (with a length of {})".format(paths_found[-1], len(paths_found[-1])))
