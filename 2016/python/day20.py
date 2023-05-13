file = open('20.txt', 'r')

ranges = []
for line in file:
    s = line.strip().split('-')
    a, b = int(s[0]), int(s[1])
    ranges.append((a,b))
file.close()

ranges.sort(key = lambda x: x[0])

ip = 0
#find first non-blocked
for r in ranges:
    if ip >= r[0] and ip <= r[1]: ip = r[1] + 1
    elif ip < r[0]: break
    
print("Lowest non-blocked:", ip)

#count them all
ip = 0
count = 0
for r in ranges:
    if ip >= r[0] and ip <= r[1]: ip = r[1] + 1
    elif ip < r[0]:
        count += r[0] - ip
        ip = r[1] + 1

    if ip > 4294967295: break

print("Total non-blocked:", count)
