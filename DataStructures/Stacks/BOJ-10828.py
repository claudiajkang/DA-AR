from sys import stdin

next(stdin)
s = list()

for line in stdin:
        c = line.split()[0]
        if c == 'push':
                s.append(line.split()[1])
        elif c == 'pop':
                if s: print(s.pop())
                else: print(-1)
        elif c == 'size':
                print(len(s))
        elif c == 'empty':
                if s: print(0)
                else: print(1)
        elif c == 'top':
                if s: print(s[-1])
                else: print(-1)
