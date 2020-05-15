from sys import stdin
read = lambda: stdin.readline().rstrip()

class Queue:
    def __init__(self):
        self.l = []
        self.f = None
        self.b = None
        self.s = 0


    def push(self, data):
        self.l.append(data)
        self.f = self.l[0]
        self.b = self.l[-1]
        self.s += 1

    def pop(self):
        if self.s:
            v = self.l.pop(0)
            self.s -= 1
            if self.s:
                self.f = self.l[0]
                self.b = self.l[-1]

            else:
                self.f = None
                self.b = None

            print(v)
        else:
            print(-1)

    def size(self):
        print(self.s)

    def empty(self):
        if self.s:
            print(0)
        else:
            print(1)

    def front(self):
        if self.s:
            print(self.f)
        else:
            print(-1)

    def back(self):
        if self.s:
            print(self.b)
        else:
            print(-1)


n = int(read())
q = Queue()

for i in range(n):
    cmd = read().split()

    if cmd[0] == 'push':
        q.push(cmd[1])

    elif cmd[0] == 'pop':
        q.pop()

    elif cmd[0] == 'size':
        q.size()

    elif cmd[0] == 'empty':
        q.empty()

    elif cmd[0] == 'front':
        q.front()

    elif cmd[0] == 'back':
        q.back()
