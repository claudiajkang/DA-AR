import queue
from sys import stdin

next(stdin)
q = queue.Queue()

for line in stdin:
    command = line.split()[0]
    if command == 'push':
        q.put(line.split()[1])
    elif command == 'pop':
        if q.qsize(): print(q.get())
        else: print(-1)
    elif command == 'size':
        print(q.qsize())
    elif command == 'empty':
        if q.qsize(): print(0)
        else: print(1)
    elif command == 'front':
        if q.qsize(): print(q.queue[0])
        else: print(-1)
    elif command == 'back':
        if q.qsize(): print(q.queue[-1])
        else: print(-1)
