from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
con = [0] * (n + 1)
singer = [[] for i in range(n + 1)]

for i in range(m):
    l = list(read())

    for j in range(1, l[0]):
        singer[l[j]].append(l[j + 1])
        con[l[j + 1]] += 1

q = deque()
res = [0] * (n + 1)

for i in range(1, n + 1):
    if con[i] == 0:
        q.append(i)

err = False
for i in range(1, n + 1):
    if not q:
        err = True
        break

    cur = q.popleft()
    res[i] = cur

    for j in singer[cur]:
        con[j] -= 1

        if con[j] == 0:
            q.append(j)

if err:
    print(0)
else:
    print('\n'.join(map(str, res[1:])))
