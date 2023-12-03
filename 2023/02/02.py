import re

file1 = open('input.txt', 'r')
lines = file1.readlines()

game_constraints = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def parse_reveal(raw_reveal):
    colors = [raw_color.strip() for raw_color in raw_reveal.split(',')]
    reveal = {}
    for color in colors:
        value, key = color.split(' ')
        reveal[key] = int(value)
    return reveal

def parse_line(line):
    split_line = re.split(':|;', line)
    id = int(split_line[0].split(' ')[1])
    reveals = [parse_reveal(raw_reveal) for raw_reveal in split_line[1:]]
    return (id, reveals)

def is_valid_reveal(reveal, constraints):
    for key, value in reveal.items():
        if not constraints.get(key) or constraints.get(key) < value:
            return False
    return True

def check_game(line, constraints):
    game_id, reveals = parse_line(line)
    for reveal in reveals:
        if not is_valid_reveal(reveal, constraints):
            return 0
    return game_id

def minimum_cubes(reveals):
    min = {}
    for reveal in reveals:
        for key, value in reveal.items():
            if not min.get(key) or min.get(key) < value:
                min[key] = value
    
    return min

def check_power(line):
    game_id, reveals = parse_line(line)
    min = minimum_cubes(reveals)
    power = 1
    for cube_count in min.values():
        power *= cube_count
    return power


id_sum = 0
power_sum = 0
for line in lines:
    id_sum += check_game(line, game_constraints)
    power_sum += check_power(line)

print(id_sum)
print(power_sum)