starts = open("15.txt", "r")
seq = starts.readline().strip().split(",")

numbers = {}
turn = 0
for n in range(0, len(seq) - 1):
    turn += 1
    numbers[int(seq[n])] = turn

last = int(seq[-1])
while turn < 2020:
    turn += 1
    if last not in numbers:
        numbers[last] = turn
        last = 0
    else:
        neckst = turn - numbers[last]
        numbers[last] = turn
        last = neckst
for k, v in numbers.items():
    if v == 2020:
        print("Part 1:", k)

while turn < 30000000:
    turn += 1
    if last not in numbers:
        numbers[last] = turn
        last = 0
    else:
        neckst = turn - numbers[last]
        numbers[last] = turn
        last = neckst
for k, v in numbers.items():
    if v == 30000000:
        print("Part 2:", k)
