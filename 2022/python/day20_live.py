file = open("20.txt", "r")

orig = []
n = 1
for line in file:
    orig.append((int(line.strip()), n))
    n += 1

file.close()
#print(new)
def shofl(orig, cycles):
    new = orig[:]
    for c in range(cycles):
        for item in orig:
            if item[0] == 0: continue
            elif item[0] > 0:
                i = new.index(item)
                new = new[i:] + new[:i]
            elif item[0] < 0:
                i = new.index(item)
                new = new[i+1:] + new[:i+1]
            a = new.pop(new.index(item))
            x = item[0] % len(new) #if item[0] > 0 else item[0] % len(new) - 1
            new.insert(x, a)
    return(new)
    #print(item)
    #print(new)
#print(new)
new = shofl(orig[:], 1)
        
new_just_data = [item[0] for item in new]
index_0 = new_just_data.index(0)
i_z_1k = new_just_data[(index_0 + 1000) % len(new)]
i_z_2k = new_just_data[(index_0 + 2000) % len(new)]
i_z_3k = new_just_data[(index_0 + 3000) % len(new)]
print("P1:", i_z_1k + i_z_2k + i_z_3k)

dec_key = 811589153
p2data = [(x[0] * dec_key, x[1]) for x in orig]
new = shofl(p2data[:], 10)

new_just_data = [item[0] for item in new]
index_0 = new_just_data.index(0)
i_z_1k = new_just_data[(index_0 + 1000) % len(new)]
i_z_2k = new_just_data[(index_0 + 2000) % len(new)]
i_z_3k = new_just_data[(index_0 + 3000) % len(new)]
print("P2:", i_z_1k + i_z_2k + i_z_3k)
