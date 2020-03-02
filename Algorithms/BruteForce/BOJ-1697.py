from collections import deque
from sys import stdin
read = lambda : stdin.readline().rstrip()

N, K = map(int, read().split())

if N == K:
    print(0)

else:
    LO = [-1 for i in range(1000001)]

    q = deque()
    q.append([N, 0])
    LO[N] = 0

    while len(q):
        cur, cd = q.popleft()

        for i in [cur-1, cur+1, cur*2]:
            if 0 <= i <= 1000000:
                if i == K:
                    LO[i] = min(LO[i], cd + 1)

                if LO[i] == -1:
                    LO[i] = cd + 1
                    q.append([i, cd + 1])

    print(LO[K])
