
class CPU:
    x = 1
    cycles = [x]
    
    def execute_cmd(self, cmd):
        if cmd[0] == 'addx':
            self.cycles += [self.x, self.x]
            self.x += int(cmd[1])
        if cmd[0] == 'noop':
            self.cycles += [self.x]

class CRT:
    def __init__(self, cpu):
        self.cpu = cpu
        self.pixels = []
    
    def print_screen(self):
        for i in range(len(self.cpu.cycles[1:])):
            pos = i % 40
            if pos == 0: 
                self.pixels.append('')
            if self.in_sprite(pos, i+1): 
                self.pixels[-1] += '#'
            else:
                self.pixels[-1] += '.'

        for line in self.pixels:
            print(line)

    def in_sprite(self, pos, time):
        return abs(self.cpu.cycles[time] - pos) <= 1


lines = open('input.txt', 'r').readlines()

cpu = CPU()
for line in lines:
    cmd = line.strip().split(' ')
    cpu.execute_cmd(cmd)

sig_strengths = []
for i in range(20, 221, 40):
    sig_strengths.append(i * cpu.cycles[i])
print(sum(sig_strengths))

crt = CRT(cpu)
crt.print_screen()
