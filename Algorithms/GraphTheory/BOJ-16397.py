from collections import deque
from sys import stdin

n, t, g = map(int, stdin.readline().rstrip().split())
btn = [-1] * (10 ** 6)

q = deque()
q.append(n)
btn[n] = 0
suc = False

while q:
    cur = q.popleft()

    if btn[cur] > t: break

    if cur == g:
        suc = True
        break

    tp = [cur + 1, cur * 2]
    for v in range(2):
        i = tp[v]
        if i > 99999 or i < 0: continue

        if v == 1:
            i -= 10 ** (len(str(i)) - 1)

        if btn[i] == -1:
            btn[i] = btn[cur] + 1
            q.append(i)

if suc:
    print(btn[g], end="")
else:
    print('ANG', end="")
