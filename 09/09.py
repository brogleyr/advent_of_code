import math
from operator import add

class Rope():
    size = 2
    knots = []
    dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    tail_coverage = []

    def __init__(self, size = 1):
        self.size = size
        self.knots = []
        self.tail_coverage = []
        for i in range(size): self.knots.append([0, 0])

    def execute(self, line):
        [dir, num] = line.strip().split(' ')
        for i in range(int(num)): self.execute_move(dir)

    def execute_move(self, dir):
        self.move_head(dir)
        for i in range(self.size - 1):
            self.move_tail(i, i+1)
        if self.knots[-1] not in self.tail_coverage: 
            self.tail_coverage.append(self.knots[-1].copy())
        #print(self.knots)

    def move_head(self, dir):
        self.knots[0] = list(map(add, self.knots[0], self.dirs[dir]))

    def move_tail(self, parent, child):
        diff = [self.knots[parent][0] - self.knots[child][0], self.knots[parent][1] - self.knots[child][1]]
        dist = abs(diff[0]) + abs(diff[1])
        if abs(diff[0]) > 1 or dist > 2: self.knots[child][0] += self.sign(diff[0])
        if abs(diff[1]) > 1 or dist > 2: self.knots[child][1] += self.sign(diff[1])
    
    def sign(self, num):
        return int(math.copysign(1, num))


lines = open('input.txt', 'r').readlines()

rope = Rope(2)
long_rope = Rope(10)
for line in lines:
    rope.execute(line)
    long_rope.execute(line)

print(len(rope.tail_coverage))
print(len(long_rope.tail_coverage))