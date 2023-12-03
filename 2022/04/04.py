import re

def create_group(line):
    bounds = re.split('-|,', line.strip())
    return [set(range(int(bounds[g]), int(bounds[g+1]) + 1)) for g in range(0, len(bounds), 2)]

lines = open('input.txt', 'r').readlines()
groups = []
for line in lines:
    groups.append(create_group(line))
subset_groups = []
intersect_groups = []
for g in groups:
    intersect = g[0] & g[1]
    if intersect in g: subset_groups.append(intersect)
    if intersect: intersect_groups.append(intersect)
print(len(subset_groups))
print(len(intersect_groups))
