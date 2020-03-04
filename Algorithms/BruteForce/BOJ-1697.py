from sys import stdin
from collections import deque
read = lambda : stdin.readline().rstrip()

P = [-1 for _ in range(10**6 + 1)]
N, K = map(int, read().split())

q = deque()
q.append([N, 0])
FINISH = False

if N == K:
    P[K] = 0

else:
    while len(q) and not FINISH:
        ci, cd = q.popleft()

        for i in [ci-1, ci+1, 2*ci]:
            if 0 <= i <= 10**6 and P[i] == -1:
                P[i] = cd + 1
                if i == K:
                    FINISH = True
                    break
                q.append([i, cd + 1])

print(P[K])
