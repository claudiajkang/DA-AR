from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
arr = [[] for i in range(n + 1)]
con = [0] * (n + 1)

for i in range(m):
    l = list(read())

    for j in range(2, l[0] + 1):
        arr[l[j - 1]].append(l[j])
        con[l[j]] += 1

q = deque()

for i in range(1, n + 1):
    if con[i] == 0:
        q.append(i)

result = [-1] * (n + 1)

for i in range(1, n + 1):
    if not q:
        print(0)
        exit()

    cur = q.popleft()
    result[i] = cur

    for j in arr[cur]:
        con[j] -= 1
        if con[j] == 0:
            q.append(j)

print('\n'.join(map(str, result[1:])))
