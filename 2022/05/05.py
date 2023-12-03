import re

def read_stack_line(line, stacks):
    f_line = line[1::4]
    i = 0
    for char in f_line:
        char_stack = stacks[i]
        if char.isalpha(): char_stack.append(char)
        i += 1
    return stacks


def build_stacks(lines):
    stack_lines = []
    i = 0
    while i < len(lines) and lines[i] and '[' in lines[i]:
        stack_lines.insert(0, lines[i])
        i += 1

    num_stacks = (len(stack_lines[0]) + 1) // 4
    stacks = []
    for i in range(num_stacks):
        stacks.append([])
    for line in stack_lines:
        read_stack_line(line, stacks)
    return stacks

def move(commands, stacks):
    from_stack = stacks[commands[1] - 1]
    to_stack = stacks[commands[2] - 1]
    for i in range(commands[0]):
        if from_stack:
            box = from_stack.pop()
            to_stack.append(box)

def move2(commands, stacks):
    from_stack = stacks[commands[1] - 1]
    to_stack = stacks[commands[2] - 1]
    if from_stack and len(from_stack) >= commands[0]:
        boxes = from_stack[-1 * commands[0]:]
        to_stack += boxes
        stacks[commands[1] - 1] = from_stack[:-1 * commands[0]]
    elif from_stack:
        to_stack += from_stack
        from_stack = []
    print(stacks)


def execute_moves(lines, stacks):
    for line in lines:
        if 'move' in line:
            commands = [int(i) for i in line.split() if i.isdigit()]
            print(commands)
            move2(commands, stacks)
        

    

f = open('input05.txt', 'r')
lines = f.readlines()
stacks = build_stacks(lines)
print(stacks)
execute_moves(lines, stacks)
tops = ''
for stack in stacks:
    tops += stack[-1]

print(tops)