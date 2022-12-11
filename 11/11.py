from operator import add, mul
from functools import reduce
from math import gcd

class Monkey:
    def __init__(self, items, op, div, targets, business):
        self.items = items
        self.op = op
        self.div = div
        self.targets = targets
        self.business = business
        self.inspected = 0

    def turn(self):
        while self.items:
            self.inspect(0)
            if self.items[0] % self.div == 0:
                self.throw(self.targets[0])
            else:
                self.throw(self.targets[1])

    def inspect(self, i):
        self.items[i] = self.op(self.items[i]) # // 3
        self.inspected += 1

    def throw(self, target):
        item = self.items.pop(0)
        self.business.monkeys[target].items.append(item)

class Business:
    monkeys = []
    lcm = 1

    def __init__(self, lines):
        monkeys = [lines[i:i+7] for i in range(0, len(lines), 7)]
        for monkey in monkeys:
            monkey = [line.split() for line in monkey]

            items = [int(item.strip(',')) for item in monkey[1][2:]]
            op = self.parse_op(monkey[2][-3:])
            div = int(monkey[3][3])
            targ = [int(monkey[4][5]), int(monkey[5][5])]

            self.monkeys.append(Monkey(items, op, div, targ, self))

        self.lcm = reduce(lambda a,b: a*b // gcd(a,b), [monkey.div for monkey in self.monkeys])

    def round(self):
        for monkey in self.monkeys: 
            monkey.turn()

    def monkey_business(self):
        scores = sorted([monkey.inspected for monkey in self.monkeys], reverse=True)
        return reduce(mul, scores[:2])

    def parse_op(self, op_line):
        increase = add if op_line[1] == '+' else self.meager_mul # mul
        if op_line[2] == 'old':
            def fun(old): return increase(old, old)
        else:
            def fun(old): return increase(old, int(op_line[2]))
        return fun

    def meager_mul(self, arg1, arg2):
        return (arg1 * arg2) % self.lcm


lines = open('input.txt', 'r').readlines()
business = Business(lines)
for i in range(10000):
    business.round()
print(business.monkey_business())
