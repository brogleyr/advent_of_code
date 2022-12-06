points = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

points2 = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 0,
    'Y': 3,
    'Z': 6
}

def score(line):
    split = line.split(' ')
    p1 = split[0].strip()
    p2 = split[1].strip()
    self_points = points[p2]
    match_points = 0
    if points[p1] == points[p2]:
        match_points = 3
    elif (points[p1] < points[p2] and not (p1 == 'A' and p2 == 'Z')) or (p1 == 'C' and p2 == 'X'):
        match_points = 6
    return self_points + match_points

def score2(line):
    split = line.strip().split(' ')
    p1, p2 = split[0], split[1]
    self_points = points2[p1]
    if p2 == 'X':
        self_points = points2[p1] - 1 if p1 != 'A' else points2['C']
    if p2 == 'Z':
        self_points = points2[p1] + 1 if p1 != 'C' else points2['A']
    return self_points + points2[p2]



f = open('input.txt', 'r')
lines = f.readlines()
scores = list(map(score2, lines))
print(scores)
print(sum(scores))