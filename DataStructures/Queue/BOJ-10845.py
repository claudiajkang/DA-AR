from sys import stdin

next(stdin)
q = list()

for line in stdin:
    command = line.split()[0]
    if command == 'push':
        v = line.split()[1]
        q.append(v)
    elif command == 'pop':
        if q: print(q.pop(0))
        else: print(-1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if q: print(0)
        else: print(1)
    elif command == 'front':
        if q: print(q[0])
        else: print(-1)
    elif command == 'back':
        if q: print(q[-1])
        else: print(-1)
