# improve input handling, namely eof detection

pps = []
passport = {}
pdata = open("04.txt", "r")
for line in pdata:
    if line == "\n":
        pps.append(passport)
        passport = {}
    else:
        passdata = line.split()
        for field in passdata:
            passport[field[0:3]] = field[4:]

valid = 0
n = 0
for passport in pps:
    n += 1
    print(n, ":", passport)
    missing = []
    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if key not in passport:
            missing.append(key)
    if missing != []:
        print("Invalid! Missing keys:", missing)
    else:
        print("Valid!")
        valid += 1
    # if missing == []: valid += 1
    
print("Valid passports:", valid)
