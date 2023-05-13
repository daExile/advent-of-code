starts = input("Puzzle input: ")
seq = starts.strip().split(",")

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
        print("Sequence", seq, ": turn 2020 is:", k)
