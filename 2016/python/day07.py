import re
#now do it all using RegEx, noob

file = open("07.txt", "r")

cTLS = cSSL = 0
for line in file:
    s = line.strip()
    a = [i.start() for i in re.finditer("[\[\]]", s)]
    hyp = ""
    seq = ""
    for i in range(0, len(a), 2):
        hyp += s[a[i]+1:a[i+1]] + " "
    a.insert(0, -1)
    for i in range(0, len(a), 2):
        try: seq += s[a[i]+1:a[i+1]] + " "
        except IndexError: seq += s[a[i]+1:]

    #TLS check
    check = True
    for i in range(len(hyp)-3):
        if hyp[i] == hyp[i+3] and hyp[i+1] == hyp[i+2] and hyp[i] != hyp[i+1]:
            check = False
    if check:
        check = False
        for i in range(len(seq)-3):
            if seq[i] == seq[i+3] and seq[i+1] == seq[i+2] and seq[i] != seq[i+1]:
                check = True
    if check: cTLS += 1

    #SSL check
    blocks = []
    for i in range(len(hyp)-2):        
        if hyp[i] == hyp[i+2] and hyp[i] != hyp[i+1] and hyp[i+1] != " ":
            blocks.append(hyp[i:i+2])
            
    for b in blocks:
        if b[1]+b[0]+b[1] in seq:
            cSSL += 1
            break

print("{} IPs support TLS.".format(cTLS))
print("{} IPs support SSL.".format(cSSL))

