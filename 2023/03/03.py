import re
import os
file1 = open(f'{os.path.dirname(__file__)}/input.txt', 'r')
lines = [line.strip() for line in file1.readlines()]


def parse_line(row, line, type):
    extracted_nums = re.findall(type.regex_pattern, line)
    numbers = []
    min_look = 0
    for extracted_num in extracted_nums:
        column = line.index(extracted_num, min_look)
        number = type(extracted_num, row, column)
        numbers.append(number)
        min_look = column + len(number)
    return numbers

def parse_lines(lines, type):
    numbers = []
    for i, line in enumerate(lines):
        numbers += parse_line(i, line, type)
    return numbers

class Part:

    regex_pattern = '[0-9]+'

    def __init__(self, number, row, column):
        self.value = int(number)
        self.row = row
        self.column = column
    
    def __len__(self):
        return len(str(self.value))
    
    def get_spaces(self):
        spaces = []
        for column in range(self.column, self.column + len(self)):
            spaces.append((column, self.row))
        return spaces
    
    def get_adjacencies(self):
        adjacencies = []
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.column - 1, self.column + len(self) + 1):
                adjacencies.append((j, i))
        self.adjacencies = adjacencies
        return adjacencies
    
    @staticmethod
    def parse_lines(lines):
        return parse_lines(lines, Part)
    
class Gear(Part):

    regex_pattern = '\*'

    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

    @staticmethod
    def parse_lines(lines):
        return parse_lines(lines, Gear)
    
    def get_attached_parts(self, lines):
        row_adj_numbers = []
        for row in range(self.row - 1, self.row + 2):
            row_adj_numbers += parse_line(row, lines[row], Part)
        
        adj_numbers = filter(
            lambda num: bool(set(num.get_spaces()) & set(self.get_adjacencies())),
            row_adj_numbers
        )
        return [num.value for num in adj_numbers]


def is_symbol_at(pos, lines):
    if pos[1] < 0 or pos[1] >= len(lines) or pos[0] < 0 or pos[0] >= len(lines[0]):
        return False
    value = lines[pos[1]][pos[0]]
    return value != '.' and not value.isdigit()

def get_part_numbers(lines):
    numbers = Part.parse_lines(lines)
    part_numbers = []
    for number in numbers:
        for position in number.get_adjacencies():
            if is_symbol_at(position, lines):
                part_numbers.append(number)
                break
    
    return [part_number.value for part_number in part_numbers]

def get_gear_ratios(lines):
    all_gears = Gear.parse_lines(lines)
    valid_gears = filter(lambda gear: len(gear.get_attached_parts(lines)) == 2, all_gears)
    ratios = []
    for gear in valid_gears:
        parts = gear.get_attached_parts(lines)
        ratios.append(parts[0] * parts[1])
    return ratios


print(sum(get_part_numbers(lines)))
print(sum(get_gear_ratios(lines)))