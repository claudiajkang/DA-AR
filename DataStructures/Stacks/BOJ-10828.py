import sys


class Stack:
    def __init__(self):
        self.s = list()
        self.size = 0

    def push(self, x):
        self.s.append(x)
        self.set_size()

    def set_size(self):
        self.size = len(self.s)

    def get_size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        return 0

    def pop(self):
        if self.size == 0:
            return -1
        v = self.s.pop()
        self.set_size()
        return v

    def top(self):
        if self.size == 0:
            return -1
        return self.s[-1]


N = int(sys.stdin.readline())
stacks = Stack()

for i in range(N):
    c = sys.stdin.readline()
    command = c.split()[0]

    if command == 'push':
        v = c.split()[1]
        stacks.push(v)
    elif command == 'pop':
        print(stacks.pop())
    elif command == 'top':
        print(stacks.top())
    elif command == 'size':
        print(stacks.get_size())
    elif command == 'empty':
        print(stacks.empty())
