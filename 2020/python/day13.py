schedule = open("13.txt", "r")
time = int(schedule.readline())
bus_list = schedule.readline().split(",")
schedule.close()

deps = []
for bus in bus_list:
    if bus == "x": continue
    else:
        deps.append([int(bus), (int(bus) - time % int(bus))])

deps.sort(key = lambda f: f[1])
print(deps)
print("First to arrive is bus #", deps[0][0], "in", deps[0][1], "min")
print("Answer:", deps[0][0] * deps[0][1])
