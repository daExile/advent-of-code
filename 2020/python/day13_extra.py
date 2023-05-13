schedule = open("13.txt", "r")
time = int(schedule.readline())
bus_list = schedule.readline().split(",")
schedule.close()

print(bus_list)
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
            print("a0 =", a0, ", step =", step)
