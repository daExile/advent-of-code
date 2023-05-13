# improve input handling, namely eof detection
import re

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
        print("Missing keys:", missing)
    else:
        if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
            missing.append("byr")
        if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
            missing.append("iyr")
        if int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
            missing.append("eyr")
        if passport["hgt"].endswith("cm"):
            if int(passport["hgt"][:-2]) < 150 or int(passport["hgt"][:-2]) > 193:
                missing.append("hgt")
        elif passport["hgt"].endswith("in"):
            if int(passport["hgt"][:-2]) < 59 or int(passport["hgt"][:-2]) > 76:
                missing.append("hgt")
        else: missing.append("hgt")
        if passport["hcl"].startswith("#") and len(passport["hcl"]) == 7:
            if re.findall("[^0-9a-f]+", passport["hcl"][1:]) != []:
                missing.append("hcl")
        else: missing.append("hcl")
        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            missing.append("ecl")
        if len(passport["pid"]) != 9 or not passport["pid"].isnumeric():
            missing.append("pid")
        if missing != []:
            print("Invalid keys:", missing)
        else:
            # print("VALID")
            valid += 1
    # if missing == []: valid += 1
    
print("Valid passports:", valid)
