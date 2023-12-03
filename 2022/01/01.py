# Using readlines()
file1 = open('input01.txt', 'r')
Lines = file1.readlines()

maxElf = 0
currElf = 0
totals = []
# Strips the newline character
for line in Lines:
    if line == '\n':
        totals.append(currElf)
        currElf = 0
    else:
        currElf += int(line)

totals.append(currElf)
totals.sort(reverse=True)
print(totals)
cals = totals[0] + totals[1] + totals[2]
print(len(totals))
print(cals)