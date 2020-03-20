from sys import stdin
read = lambda: stdin.readline().rstrip()

class Deque:
    def __init__(self):
        self.l = []
        self.f = None
        self.b = None
        self.s = 0


    def push_front(self, data):
        self.l.insert(0, data)
        self.f = self.l[0]
        self.b = self.l[-1]
        self.s += 1


    def push_back(self, data):
        self.l.append(data)
        self.f = self.l[0]
        self.b = self.l[-1]
        self.s += 1


    def pop_front(self):
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


    def pop_back(self):
        if self.s:
            v = self.l.pop()
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
dq = Deque()

for i in range(n):
    cmd = read().split()

    if cmd[0] == "push_front":
        dq.push_front(cmd[1])

    elif cmd[0] == "push_back":
        dq.push_back(cmd[1])

    elif cmd[0] == "front":
        dq.front()

    elif cmd[0] == "back":
        dq.back()

    elif cmd[0] == "empty":
        dq.empty()

    elif cmd[0] == "pop_front":
        dq.pop_front()

    elif cmd[0] == "pop_back":
        dq.pop_back()

    elif cmd[0] == "size":
        dq.size()
