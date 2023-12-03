import string

def find_common(line):
    p1 = line[:len(line)//2]
    p2 = line[len(line)//2:]
    return list(set(p1) & set(p2))[0]

def find_common_group(lines):
    common_set = None
    for elf in  lines:
        elf_set = set(elf.strip())
        common_set = elf_set & common_set if common_set else elf_set
    return list(common_set)[0]

def find_score(type):
    priority = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53)))
    return priority[type]

f = open('input.txt', 'r')
lines = f.readlines()

scores = []
for line in lines:
    scores.append(find_score(find_common(line)))
print(sum(scores))

scores2 = []
print(len(lines))
for i in range(0, len(lines), 3):
    if lines[i: i+3]: scores2.append(find_score(find_common_group(lines[i:i+3])))
    print(i)
print(sum(scores2))

