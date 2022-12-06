def find_marker_pos(line):
    i = 0
    while i < len(line) - 4:
        slice = line[i:i+4]
        unique = True
        for char in slice:
            if slice.count(char) > 1:
                unique = False
                break
        if unique:
            return i + 4
        i += 1
    return -1

def find_marker_pos2(line):
    i = 0
    while i < len(line) - 14:
        slice = line[i:i+14]
        unique = True
        for char in slice:
            if slice.count(char) > 1:
                unique = False
                break
        if unique:
            return i + 14
        i += 1
    return -1
            


f = open('input.txt', 'r')
line = f.readline()

print(find_marker_pos2(line))