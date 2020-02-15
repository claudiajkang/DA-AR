from sys import stdin

next(stdin)
q = list()

for line in stdin:
        c = line.split()[0]
        if c == 'push':
                q.append(line.split()[1])
        elif c == 'pop':
                if q: print(q.pop(0))
                else: print(-1)
        elif c == 'size':
                print(len(q))
        elif c == 'empty':
                if q: print(0)
                else: print(1)
        elif c == 'front':
                if q: print(q[0])
                else: print(-1)
        elif c == 'back':
                if q: print(q[-1])
                else: print(-1)
