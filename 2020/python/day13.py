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
print("Part 1:", deps[0][0] * deps[0][1])

a = a0 = 0
step = 1
for n in range(0,len(bus_list)):
    if bus_list[n] == "x": continue
    else:
        bus_id = int(bus_list[n])
        a = a0
        delta = (-n) % bus_id
        while a % bus_id != delta:
            a += step
        else:
            a0 = a
            step *= bus_id
print("Part 2:", a0)
