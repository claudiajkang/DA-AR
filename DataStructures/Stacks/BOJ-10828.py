from sys import stdin
read = lambda: stdin.readline().rstrip()


class Stack:
    def __init__(self):
        self.l = []
        self.t = None
        self.s = 0

    def push(self, data):
        self.l.append(data)
        self.t = self.l[-1]
        self.s += 1

    def pop(self):
        if self.s:
            v = self.l.pop()
            self.s -= 1
            if self.s:
                self.t = self.l[-1]
            else:
                self.t = None
            return v
        else:
            return -1

    def size(self):
        return self.s

    def empty(self):
        if self.s:
            return 0
        else:
            return 1

    def top(self):
        if self.s:
            return self.t
        else:
            return -1


n = int(read())
st = Stack()

for i in range(n):
    cmd = read().split()

    if cmd[0] == "push":
        st.push(cmd[1])

    elif cmd[0] == "top":
        print(st.top())

    elif cmd[0] == "size":
        print(st.size())

    elif cmd[0] == "pop":
        print(st.pop())

    elif cmd[0] == "empty":
        print(st.empty())

