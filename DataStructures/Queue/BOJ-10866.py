from sys import stdin

next(stdin)
d = list()

for line in stdin:
    c = line.split()[0]
    if c == 'push_front':
        d.insert(0, line.split()[1])
    elif c == 'push_back':
        d.append(line.split()[1])
    elif c == 'pop_front':
        if d: print(d.pop(0))
        else: print(-1)
    elif c == 'pop_back':
        if d: print(d.pop())
        else: print(-1)
    elif c == 'size':
        print(len(d))
    elif c == 'empty':
        if d: print(0)
        else: print(1)
    elif c == 'front':
        if d: print(d[0])
        else: print(-1)
    elif c == 'back':
        if d: print(d[-1])
        else: print(-1)
