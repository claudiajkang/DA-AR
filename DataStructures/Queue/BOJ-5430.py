from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

t = int(read())

for _ in range(t):
    p = read()
    n = int(read())
    arr = read()
    arr = arr[1:-1]
    if arr:
        arr = arr.split(',')
    q = deque(arr)

    rvs = False
    err = 0

    for i in p:
        if i == "R":
            rvs = not rvs

        elif i == "D":
            if q:
                if rvs:
                    q.pop()
                else:
                    q.popleft()
            else:
                err = 1
                break

    if err:
        print("error")
    else:
        if rvs:
            q.reverse()
        print("[", end = "")
        lq = len(q)
        for i in range(lq):
            if i == lq-1:
                print(q.popleft(), end="")
            else:
                print(q.popleft(), end=",")
        print("]")